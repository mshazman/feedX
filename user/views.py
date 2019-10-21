import os
from django.shortcuts import render
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from quiz.models import Quiz
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from scripts import git_pull


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

'''function for displaying events of user and events that user can participate in'''
def dashboard(request):
    print(request.user)
    other_events = Quiz.objects.exclude(owner__username=str(request.user))
    live_events = [
                    {'status':result.is_participant(request.user.id),
                    'live': result
                    }
                    for result in other_events
                  ]
    quiz = request.user.quiz_set.all()
    context = {
        'participation':live_events,
        'quiz':quiz,
    }
    return render(request, 'user/dashboard.html',context)


def test(request,filename,id=0, hex=0):
    filepath = os.path.join(os.getcwd(),'quiz/templates/quiz/'+filename)
    id = str(id)
    if id.startswith('q'):
        quiz=Quiz.objects.get(quiz_id=id)
        questions = quiz.questions.all()
    else:
        questions={}
    context = {
        'id':id,
        'hex':hex,
        'questions':questions
    }
    with open(filepath, 'r') as file:
        content = file.read()
    return render(request,f'quiz/{filename}',context)


'''404 custom error handling'''
def handler404(request,exception):
    return render(request, '404.html', status=404)

'''500 custom error handling'''
def handler500(request):
    return render(request, '500.html', status=500)


