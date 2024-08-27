from typing import Any
from django.views import View
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from vaccine.models import Vaccine
from campaign.models import Campaign, Slot
from vaccination.forms import Vaccination_Form
from django.utils import timezone
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from vaccination.models import Vaccination
from vaccination.utils import generate_pdf
from django.contrib.auth.decorators import login_required

# Create your views here.
class Choose_Vaccine(LoginRequiredMixin, generic.ListView):
    model = Vaccine
    template_name = "vaccination/choose_vaccine.html"
    paginate_by = 10
    ordering = ["name"]
class Choose_Campaign(LoginRequiredMixin, generic.ListView):
    model = Campaign
    template_name = "vaccination/choose_campaign.html"
    paginate_by = 10
    ordering = ["center"]
    
    def get_queryset(self):
        return super().get_queryset().filter(vaccine_id = self.kwargs["vaccine_id"])
    
class Choose_Slot(LoginRequiredMixin, generic.ListView):
    model = Slot
    template_name = "vaccination/choose_slot.html"
    paginate_by = 10
    ordering = ['date']
    def get_queryset(self):
        return super().get_queryset().filter(campaign_id = self.kwargs["campaign_id"], date = timezone.now())

class Confirm_Vaccination(View):
    form_class = Vaccination_Form
    
    def get(self, request, *args, **kwargs):
        campaign = Campaign.objects.get(id = self.kwargs["campaign_id"])
        slot = Slot.objects.get(id = self.kwargs["slot_id"])
        form = self.form_class(initial={
            "patient": request.user,
            "campaign": campaign,
            "slot": slot,
        })
        context = {
            "patient": request.user,
            "campaign": campaign,
            "form": form
        }
        return render(request, "vaccination/confirm_vaccination.html", context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            is_reserved = Slot.reserve_vaccine(self.kwargs["campaign_id"], self.kwargs["slot_id"])
            if is_reserved:
                form.save()
                return HttpResponse("Your vaccination has been scheduled")
            return HttpResponseBadRequest("Unable to schedule the vaccination!")
        return HttpResponseBadRequest("Invalid form data")


class Vaccination_List(LoginRequiredMixin, generic.ListView):
    model = Vaccination
    template_name = "vaccination/vaccination_list.html"
    paginate_by = 10
    ordering = ["id"]
    
    def get_queryset(self):
        return super().get_queryset().filter(patient = self.request.user)
    
class Vaccination_Details(LoginRequiredMixin, generic.DetailView):
    model = Vaccination
    template_name = "vaccination/vaccination_details.html"
    
@login_required
def appointment_leter(request, vaccination_id):
    vaccination = Vaccination.objects.get(id = vaccination_id)
    context = {
        "pdf_title": f"{vaccination.patient.get_full_name()} | Appointment Letter",
        "date": str(timezone.now()),
        "title": "Appointment Letter",
        "subtitle": "To whom it may concern",
        "content": f"This is to inform that the {vaccination.campaign.vaccine.name} vaccination of Mr/Ms {vaccination.patient.get_full_name()} is scheduled on {vaccination.slot.date}"
        
    }
    return generate_pdf(context)

@login_required
def vaccination_certificate(request, vaccination_id):
    vaccination = Vaccination.objects.get(id = vaccination_id)
    if vaccination.is_Vaccinated:
        context = {
            "pdf_title": f"{vaccination.patient.get_full_name()} | Vaccination Certificate",
            "date": str(timezone.now()),
            "title": "Vaccination Certificate",
            "subtitle": "to whom it may concern",
            "content": f"This is to certify that Mr/Ms {vaccination.patient.get_full_name()} has successfully taken the {vaccination.campaign.vaccine.name} on {vaccination.date}. The vaccination was sceduled on {vaccination.slot.date} {vaccination.slot.start_time} at {vaccination.campaign.center.name}"
        }
        return generate_pdf(context)
    return HttpResponseBadRequest("User is not vaccinated")