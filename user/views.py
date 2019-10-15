from django.shortcuts import render
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')
    success_message = "Account created. Now you can login!!"

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = '/'


def dashboard(request):
    return render(request, 'user/temp.html')