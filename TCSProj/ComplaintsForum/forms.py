from django import forms
from .models import Complaint
from django.forms import ModelForm, Textarea


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = '__all__'
        widgets = {
            'complaint_description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        print fields
        # print("jaclin")

        def __init__(self):
            self.fields['first_name'].label = "First Name"
