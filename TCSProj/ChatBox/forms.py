from django import forms #django already has a class called forms

from ComplaintsForum.models import Chat,Client,Provider
from django.contrib.auth.models import User

from ComplaintsForum.models import Employee

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    #first_name = forms.CharField(required=True,label="Commpany")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model=Employee
        fields=['username','email','password','company','customer','provider']

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
