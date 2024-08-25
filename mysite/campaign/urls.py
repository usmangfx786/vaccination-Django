from django.urls import path
from campaign import views

app_name = "campaign"

urlpatterns = [
    path("", views.Campaign_List_View.as_view(), name="campaign_list"),
    path("<int:pk>/", views.Campaign_Detail_View.as_view(), name="campaign_details"),
    path("create/", views.Campaign_Create_View.as_view(), name="campaign_create"),
    path("update/<int:pk>/", views.Campaign_Update_View.as_view(), name="campaign_update"),
    path("delete/<int:pk>/", views.Campaign_Delete_View.as_view(), name="campaign_delete"),
    path("<int:campaign_id>/slot/", views.Slot_List_View.as_view(), name="slot_list"),
    path("slot/<int:pk>/", views.Slot_Details_View.as_view(), name="slot_details"),
]
