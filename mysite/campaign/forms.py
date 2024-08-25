from django.forms import ModelForm
from campaign.models import Campaign

class Campaign_Model_Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Campaign_Model_Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = 'form-control'
    class Meta:
        model = Campaign
        fields = "__all__"
        