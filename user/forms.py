from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    name = forms.CharField(max_length=20,label='Full-Name')

    class Meta:
        model = User
        fields = ['name','email','password1','password2']


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'Full name'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirm Password'})