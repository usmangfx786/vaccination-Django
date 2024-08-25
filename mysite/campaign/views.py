from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from campaign.models import Campaign
from vaccination.models import Vaccination
from campaign.models import Slot
from campaign.forms import Campaign_Model_Form
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.

class Campaign_List_View(LoginRequiredMixin, generic.ListView):
    model = Campaign
    template_name = "campaign/campaign_list.html"
    paginate_by = 10
    ordering = ["-id"]
    

class Campaign_Detail_View(LoginRequiredMixin, generic.DetailView):
    model = Campaign
    template_name = "campaign/campaign_details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Registration"] = Vaccination.objects.filter(campaign=self.kwargs["pk"]).count()
        return context
    

class Campaign_Create_View(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Campaign
    form_class = Campaign_Model_Form
    permission_required = ("campaign.add_campaign",)
    template_name = "campaign/campaign_create.html"
    success_url = reverse_lazy("campaign:campaign_list")
    success_message = "Campaign Created Successfully"
    
    
class Campaign_Update_View(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Campaign
    form_class = Campaign_Model_Form
    permission_required = ("campaign.change_campaign",)
    template_name = "campaign/campaign_update.html"
    success_url = reverse_lazy("campaign:campaign_list")
    success_message = "Capmaign Updated Successfully"
    

class Campaign_Delete_View(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Campaign
    permission_required = ("campaign.delete_campaign")
    template_name = "campaign/campaign_delete.html"
    success_url = reverse_lazy("campaign:campaign_list")
    success_message = "Campaign Deleted Successfully"

class Slot_List_View(LoginRequiredMixin, generic.ListView):
    model = Slot
    template_name = "campaign/slot_list.html"
    paginate_by = 10
    def get_queryset(self):
        queryset = Slot.objects.filter(campaign = self.kwargs["campaign_id"]).order_by("id")
        return queryset
    

class Slot_Details_View(LoginRequiredMixin, generic.DetailView):
    model = Slot
    template_name = "campaign/slot_details.html"