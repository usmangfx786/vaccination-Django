from django.urls import path
from center import views
app_name = 'center'
urlpatterns = [
    path("", views.center_list, name='list'),
    path("<int:id>/", views.center_details, name='details'),
    path("create/", views.create_center, name='create'),
    path("update/<int:id>/", views.update_center, name="update"),
    path("delete/<int:id>/", views.delete_center, name="delete"),
    path("<int:center_id>/storage/", views.Storage_List.as_view(), name="storage"),
    path("storage/<int:pk>/", views.Storage_Details.as_view(), name="storage_detail"),
    path("<int:center_id>/storage/create/", views.Create_Storage.as_view(), name="create_storage"),
    path("storage/update/<int:pk>/", views.Update_Storage.as_view(), name="update_storage"),
    path("storage/delete/<int:pk>/", views.Delete_Storage.as_view(), name="delete_storage"),
]
