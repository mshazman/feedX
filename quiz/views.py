import json
import secrets
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from quiz.forms import QuizForm
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import generics
from quiz.serializers import *
from . models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class QuestionPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page'
    max_page_size = 1


class ListQuizView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(quiz_id = 'q' +secrets.token_hex(8))

class DetailQuizView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class ListQusetionView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['quiz']
    pagination_class = QuestionPagination
    # def perform_create(self, serializer):
    #     serializer.save(ques_id = 'u' +secrets.token_hex(8))


class DetailQuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ListChoiceView(generics.ListCreateAPIView):
    queryset = QuestionChoice.objects.all()
    serializer_class = ChoiceSerializer

    filterset_fields = ['ques_id']


class DetailChoiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionChoice.objects.all()
    serializer_class = ChoiceSerializer


class ListAnswerView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filterset_fields = ['ques_id']


class DetailAnswerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ListSubmissionView(generics.ListCreateAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = SubmissionSerializer
    filterset_fields = ['ques_id', 'user', 'quiz']


class DetailSubmissionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = SubmissionSerializer


def generate_id(self):
        return JsonResponse({'id': str(secrets.token_hex(8))})


def event(request,id=''):
    quiz = Quiz.objects.get(quiz_id=id)
    questions = quiz.questions.all()
    # print(questions.choices.all())
    context = {
        'question':questions,
    }
    return render(request,'quiz/participate.html',context)


@csrf_exempt
def new_quiz(request):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            print(data)
    return json.dumps(request.body)


@csrf_exempt
def answerForm(request):
    if request.method == 'POST':
        if request.body:
            print(request.body)
            data = json.loads(request.body)#jsonresponser of the submitted form
            print(data['answer'])
            return HttpResponse(request.body)


