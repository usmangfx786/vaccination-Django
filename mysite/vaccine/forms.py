from django.forms import ModelForm
from vaccine.models import Vaccine


class Vaccine_Form(ModelForm):
    class Meta:
        model = Vaccine
        fields = "__all__"
