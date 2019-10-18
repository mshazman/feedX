import json
import secrets
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from quiz.forms import QuizForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
class CreateQuizView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    form_class = QuizForm
    template_name = 'quiz/create_quiz.html'
    success_url = reverse_lazy('dashboard')
    success_message = "Quiz Created"

    def form_valid(self, form):
       form.instance.owner = self.request.user
       form.instance.quiz_id = form.generate_id()
       return super().form_valid(form)

def generate_id(self):
        return JsonResponse({'id': str(secrets.token_hex(8))})
