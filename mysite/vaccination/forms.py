from django import forms
from vaccination.models import Vaccination

class Vaccination_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Vaccination_Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget = forms.HiddenInput()
    class Meta:
        model =  Vaccination
        fields = ["patient", "campaign", "slot"]
        labels = {
            "campaign": "Vaccine / Canter Name",
            "slot": "Date / Slot"
        }