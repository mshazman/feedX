from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account created. Now you can login!!')
            print("form is validated")
            return redirect('login')
    else:
        form = UserRegistrationForm()
        print("form is not validated!!")
    return render(request,'user/register.html',{'form':form})

def dashboard(request):
    return render(request, 'user/dashboard.html')

