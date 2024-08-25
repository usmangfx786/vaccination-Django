from django.urls import path
from user import views

app_name = "user"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("change-password/", views.change_password, name="change_password"),
    path("profile-view/", views.profile_view, name="profile_view"),
    path("profile-update/", views.profile_update, name="profile_update"),
    path("varify-email/", views.email_varification_request, name="varify_email"),
    path("email/activate/<uidb64>/<token>/", views.email_verifier, name="email_activate"),
]
