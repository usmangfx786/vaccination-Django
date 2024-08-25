from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from vaccine.models import Vaccine
from django.http import Http404
from vaccine.forms import Vaccine_Form
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required, name="dispatch")
class Vaccine_list(View):
    def get(self, request):
        vaccine_list  = Vaccine.objects.all().order_by("name")
        paginator = Paginator(vaccine_list, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj": page_obj
        }
        return render(request, "vaccine/vaccine_list.html", context)


@method_decorator(login_required, name="dispatch")
class Vaccine_detail(View):
    def get(self, request, id):
        try:
            vaccine = Vaccine.objects.get(id = id)
        except Vaccine.DoesNotExist:
            raise Http404("Vaccine is not found")
        context = {
            "object": vaccine
        }
        return render(request, "vaccine/vaccine_detail.html", context)


@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("vaccine.add_vaccine", raise_exception=True), name="dispatch")
class Create_vaccine(View):
    form_class = Vaccine_Form
    template_name = "vaccine/create_vaccine.html"

    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, self.template_name, context)
    
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaccine created successfully")
            return redirect("vaccine:list")
        messages.error(request, "Vaccine data is invalid")
        return render(request, self.template_name, {"form": form})
         
            
@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("vaccine.change_vaccine", raise_exception=True), name="dispatch")
class Update_Vaccine(View):
    form_class = Vaccine_Form
    template_name = "vaccine/update_vaccine.html"
    
    def get(self, request, id):
        vaccine = get_object_or_404(Vaccine, id = id)
        context = {
            "form": self.form_class(instance=vaccine)
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        form = self.form_class(request.POST, instance = vaccine)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaccine updated successfully")
            return redirect("vaccine:details", id = vaccine.id)
        messages.error(request, "Vaccine data is invalid")
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("vaccine.delete_vaccine", raise_exception=True), name="dispatch")
class Delete_Vaccine(View):
    template_name = "vaccine/delete_vaccine.html"
    
    def get(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        context = {
            "object": vaccine
        }
        return render(request, self.template_name, context)
    
    
    def post(self, request, id):
        Vaccine.objects.filter( id= id).delete()
        messages.success(request, "Vaccine deleted successfully")
        return redirect("vaccine:list")