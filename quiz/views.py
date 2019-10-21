import json
import secrets
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from quiz.serializers import *
from . models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination



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


# def event(request,id=''):
#     quiz = Quiz.objects.get(quiz_id=id)
#     questions = quiz.questions.all()
#     # print(questions.choices.all())
#     context = {
#         'question':questions,
#     }
#     return render(request,'quiz/participate.html',context)


@csrf_exempt
def new_quiz(request):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            print(data)
    return json.dumps(request.body)



def take_quiz(request, id):
    quiz = Quiz.objects.get(quiz_id=id)
    context ={
        'quiz':quiz
    }
    return render(request,'quiz/participate.html', context)


@csrf_exempt
def answerForm(request):
    if request.method == 'POST':
        if request.body:
            print(request.body)
            data = json.loads(request.body)#jsonresponser of the submitted form
            print(data['answer'])
            return HttpResponse(request.body)


@csrf_exempt
def quiz_template_render(request, filename):

    if request.method=='POST':
        if request.body:
            data = json.loads(request.body)
            next_page = data['next']
            question = data['results'][0]
            choices = data['results'][0]['choices'];

            context = {
                'next': next_page,
                'question': question,
                'choices': choices,
            }
    else:
        context = {}

    return render(request,f'quiz/{filename}',context)


def quiz_result(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    print(quiz)
    participants = quiz.get_participants()
    results = []
    for participant in participants:
        participant_result = quiz.get_score(participant['user__id'])
        participant_result['id'] = participant['user__id']
        participant_result['name'] = participant['user__first_name']
        participant_result['username'] = participant['user__username']
        results.append(participant_result)

    return render(request, 'quiz/results.html', {'quiz': quiz, 'results':results})


