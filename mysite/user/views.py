from django.shortcuts import render, redirect
from user.models import User
from django.contrib import messages
from user.forms import SignUpForm, LoginForm, Change_Password_Form, Profile_Update_Form
from django.contrib.auth import authenticate, login as User_login, logout as User_logout, update_session_auth_hash
from user.email import send_email_varification
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth import get_user_model
from user.utils import EmailVarificationTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Account Created Successfully! Please Login")
            return redirect("index")
        messages.error(request, "Invalid Data")
        return render(request, "user/signup_form.html", {"form": form})
    context = {
        "form": SignUpForm()
    }
    return render(request, "user/signup_form.html", context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email = email, password = password)
            if user is not None:
                User_login(request, user)
                messages.success(request, "Login Successfull")
                return redirect("index")
            messages.error(request, "please enter valid credentials")
            return redirect("accounts/login")
        messages.error(request, "Please enter valid credentials")
        return redirect("accounts:login")
    context = {
        "form": LoginForm()
    }
    return render(request, 'user/login_form.html', context)

@login_required
def logout(request):
    User_logout(request)
    messages.info(request, "Loged out successfully")
    return redirect("user:login")

@login_required
def change_password(request):
    if request.method == "POST":
        form = Change_Password_Form(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "password changed successfully")
            return redirect("index")
        messages.error(request, "please enter valid data")
        return render(request, "user/change_password.html", {"form":form})
    # GET
    context = {
        "form": Change_Password_Form(request.user)
    }
    return render(request, "user/change_password.html", context)

@login_required
def profile_view(request):
    context = {
        "user": request.user
    }
    return render(request, "user/profile_view.html", context)

@login_required
def profile_update(request):
    if request.method == "POST":
        form = Profile_Update_Form(request.POST, request.FILES, instance= request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect("user:profile_view")
        messages.error(request, "please enter valid data")
        return render(request, "user/profile_update.html", {"form":form})
    context = {
        'form': Profile_Update_Form(instance = request.user)
    }
    return render(request, "user/profile_update.html", context)

@login_required
def email_varification_request(request):
    if not request.user.is_email_verified:
        send_email_varification(request, request.user.id)
        return HttpResponse("Email varification link sent to your email address")
    return HttpResponseForbidden("Email is already varified")

@login_required
def email_verifier(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id = uid)
    except User.DoesNotExist:
        user = None
    if user == request.user:
        if EmailVarificationTokenGenerator.check_token(user, token):
            user.is_email_verified = True
            user.save()
            messages.success(request, "Email address is varified successfully")
            return redirect("user:profile_view")
        return HttpResponseBadRequest("invalid request")
    return HttpResponseForbidden("You dont have permission to use this link")
        