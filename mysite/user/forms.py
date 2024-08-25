from typing import Any
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
User = get_user_model()

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = 'form-control'
            
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "gender",
            "photo",
            "identity_document_type",
            "identity_document_number",
        ]
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(self, *args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    class Meta:
        model = User
        fields = '__all__'
        
class Change_Password_Form(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(Change_Password_Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    class Meta:
        model = User
        fields = "__all__"

class Profile_Update_Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Profile_Update_Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "photo",
            "date_of_birth",
            "identity_document_type",
            "identity_document_number",
        ]