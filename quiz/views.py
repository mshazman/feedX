from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from quiz.forms import QuizForm
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