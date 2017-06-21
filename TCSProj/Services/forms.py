from django import forms
from ComplaintsForum.models import Service, Company, SLA, Client
from django.forms import ModelForm, Textarea

class SLAForm(forms.ModelForm):

    class Meta:
        model = SLA
        fields = '__all__'
        print ("" + fields)

        def __init__(self):
            self.fields['service_name'].label = "Service Name"