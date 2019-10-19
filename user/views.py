import os
from django.shortcuts import render
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from quiz.models import Quiz, QuestionType
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from  django.contrib.admin.views.decorators import staff_member_required
from scripts import  git_pull


@staff_member_required
def pull_url(request):
   message = git_pull()
   return JsonResponse({'status':message})

def index(request):
    return render(request,'index.html')

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
    print(request.user)
    live_events = Quiz.objects.exclude(owner=request.user)
    quiz = request.user.quiz_set.all()
    context = {
        'quiz':quiz,
        'live':live_events
    }
    print(live_events)
    return render(request, 'user/dashboard.html',context)

def test(request,filename,id=0, hex=0):
    filepath = os.path.join(os.getcwd(),'quiz/templates/quiz/'+filename)
    context = {
        'id':id,
        'hex':hex
    }
    with open(filepath, 'r') as file:
        content = file.read()
    return render(request,f'quiz/{filename}',context)

def testfunction(request):
    return render(request, 'user/test.html')
