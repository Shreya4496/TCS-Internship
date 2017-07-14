from django import forms #django already has a class called forms

from ComplaintsForum.models import Chat,Client,Provider
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']

class ServiceProvider(forms.ModelForm):

    class Meta:
        model = Provider
        fields = '__all__'

        def __init__(self):
            self.fields['provider_name'].label = "Provider Name"


class Customer(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

        def __init__(self):
            self.fields['client_name'].label = "Client Name"
