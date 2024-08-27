from django.urls import path
from vaccination import views
 
app_name = 'vaccination'

urlpatterns = [
    path("", views.Vaccination_List.as_view(), name="vaccination_list"),
    path("choose-vaccine/", views.Choose_Vaccine.as_view(), name="choose_vaccine"),
    path("appointment-letter/<int:vaccination_id>/", views.appointment_leter, name="appointment_letter"),
    path("vaccination-certificate/<int:vaccination_id>/", views.vaccination_certificate, name="vaccination_certificate"),
    path("choose-campaign/<int:vaccine_id>/", views.Choose_Campaign.as_view(), name="choose_campaign"),
    path("choose-slot/<int:campaign_id>/", views.Choose_Slot.as_view(), name="choose_slot"),
    path("confirm-vaccination/<int:campaign_id>/<int:slot_id>/", views.Confirm_Vaccination.as_view(), name="confirm_vaccination"),
    path("vaccination-details/<int:pk>/", views.Vaccination_Details.as_view(), name="vaccination_details"),
]
