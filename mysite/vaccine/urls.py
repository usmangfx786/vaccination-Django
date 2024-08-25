from django.urls import path
from vaccine import views
app_name = "vaccine"
urlpatterns = [
    path('', views.Vaccine_list.as_view(), name= 'list' ),
    path('<int:id>/', views.Vaccine_detail.as_view(), name= 'details' ),
    path('create/', views.Create_vaccine.as_view(), name= 'create' ),
    path('update/<int:id>/', views.Update_Vaccine.as_view(), name='update'),
    path('delete/<int:id>/', views.Delete_Vaccine.as_view(), name='delete'),

]
