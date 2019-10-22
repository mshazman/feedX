from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm


class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=20, label='Full-Name')

    class Meta:
        model = User

        fields = ['username', 'name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Full name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':"form-control", 'placeholder':'Username', 'id':'inputEmail'})
        self.fields['password'].widget.attrs.update({'class':"form-control", 'placeholder':"Password", 'id':'inputPassword'})

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':"form-control", 'placeholder':"Email-Id"})

class UserSetNewPassword(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class':"form-control", 'placeholder':"New Password"})
        self.fields['new_password2'].widget.attrs.update({'class':"form-control", 'placeholder':"Confirm Password"})
