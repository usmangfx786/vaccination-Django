from django.forms import ModelForm
from campaign.models import Campaign, Slot

class Campaign_Model_Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Campaign_Model_Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = 'form-control'
    class Meta:
        model = Campaign
        fields = "__all__"

class Slot_Form(ModelForm):
    def __init__(self, campaign_id, *args, **kwargs):
        super(Slot_Form, self).__init__(*args, **kwargs)
        self.fields["campaign"].queryset.filter(id = campaign_id)
        self.fields["campaign"].disabled = True
        self.fields["reserved"].disabled = True
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = 'form_control'   
    class Meta:
        model = Slot
        fields = '__all__'