from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from center.models import Center, Storage
from center.forms import center_form, storage_form
from django.views import generic
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
@login_required
def center_list(request):
    objects = Center.objects.all().order_by("name")
    paginator = Paginator(objects, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'center/center_list.html', context)

@login_required
def center_details(request, id):
    object = Center.objects.get(id = id)
    context = {
        "center": object
    }
    return render(request, "center/center_detail.html", context)

@login_required
@permission_required("center.add_center", raise_exception=True)
def create_center(request):
    if request.method == "POST":
        form = center_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaccination center created successfully")
            return redirect('center:list')
        messages.error(request, "center data is invalid")
        return render(request, 'center/create_center.html', {'form':form})
    context = {
        "form": center_form
    }
    return render(request, 'center/create_center.html', context)

@login_required
@permission_required("center.change_center", raise_exception=True)
def update_center(request, id):
    try:
        center = Center.objects.get(id = id)
    except Center.DoesNotExist:
        raise Http404("Center is not found")
    if request.method == "POST":
        form = center_form(request.POST, instance= center)
        if form.is_valid:
            form.save()
            messages.success(request, "Center has been Updated Successfully")
            return redirect("center:details", id = center.id)
        messages.error(request, "Center data is invalid")
        return render(request, "center/update_center.html", {"form":form})
    context = {
        "form" : center_form(instance = center)
    }
    return render(request, "center/update_center.html", context)

@login_required
@permission_required("center.delete_center", raise_exception=True)
def delete_center(request, id):
    try:
         center = Center.objects.get(id = id)
    except Center.DoesNotExist:
        raise ("Center is not found") 
    if request.method == "POST":
        center.delete()
        messages.success(request, "Center deleted")
        return redirect("center:list")
    context = {
        "center": center
    }
    return render(request, "center/delete_center.html", context)




class Storage_List(LoginRequiredMixin, generic.ListView):
    queryset = Storage.objects.all()
    template_name = 'storage/storage_list.html'
    ordering = ["id"]
    paginate_by = 2
    
    def get_queryset(self):
        return super().get_queryset().filter(center_id = self.kwargs["center_id"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["center_id"] = self.kwargs['center_id'] 
        return context
    



class Storage_Details(LoginRequiredMixin, generic.DetailView):
    model = Storage
    template_name = 'storage/storage_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_quantity"] = self.object.total_quantity - self.object.booked_quantity
        return context



class Create_Storage(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Storage
    form_class = storage_form
    template_name = 'storage/create_storage.html'
    success_message = "Storage created successfully"
    permission_required = ("center.add_storage",)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["center_id"] = self.kwargs["center_id"]
        return kwargs
    
    def get_initial(self):
        initial = super().get_initial()
        initial["center"] = Center.objects.get(id= self.kwargs['center_id'])
        return initial
    
    def get_success_url(self):
        return reverse("center:storage", kwargs={"center_id": self.kwargs["center_id"]})
    
class Update_Storage(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Storage
    form_class = storage_form
    template_name = "storage/storage_update.html"
    success_message = "Storage updated successfully"
    permission_required = ("center.change_storage",)


    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["center_id"] = self.get_object().center.id
        return kwargs
    
    def get_success_url(self):
        return reverse('center:storage', kwargs={'center_id': self.get_object().center.id})
    
    
class Delete_Storage(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Storage
    template_name = "storage/delete_storage.html"
    success_message = "Storage deleted successfully"
    permission_required = ("center.delete_storage",)


    
    def get_success_url(self):
        return reverse("center:storage", kwargs={"center_id": self.get_object().center.id})