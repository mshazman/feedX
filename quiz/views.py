import json
import secrets
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from quiz.serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator

'''API Starts here'''


class QuestionPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page'
    max_page_size = 1


class ListQuizAPI(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(quiz_id='q' + secrets.token_hex(8))


class DetailQuizAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class ListQusetionAPI(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['quiz']
    pagination_class = QuestionPagination


class DetailQuestionAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ListChoiceAPI(generics.ListCreateAPIView):
    queryset = QuestionChoice.objects.all()
    serializer_class = ChoiceSerializer
    filterset_fields = ['ques_id']


class DetailChoiceAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionChoice.objects.all()
    serializer_class = ChoiceSerializer


class ListAnswerAPI(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filterset_fields = ['ques_id']


class DetailAnswerAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ListSubmissionAPI(generics.ListCreateAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = SubmissionSerializer
    filterset_fields = ['ques_id', 'user', 'quiz']


class DetailSubmissionAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = SubmissionSerializer


'''API ends here'''


def generate_id(self):
    return JsonResponse({'id': str(secrets.token_hex(8))})


@csrf_exempt
def new_quiz(request):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
    return json.dumps(request.body)


def take_quiz(request, id):
    quiz = Quiz.objects.get(quiz_id=id)
    context = {
        'quiz': quiz
    }
    return render(request, 'quiz/participate.html', context)


@csrf_exempt
def answer_form(request):
    if request.method == 'POST':
        if request.body:
            # Json response of the submitted form
            # data = json.loads(request.body)
            # print(data['answer'])
            return HttpResponse(request.body)


@csrf_exempt
def quiz_template_render(request, filename):
    context = {}
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            question = data
            choices = data['choices']

            context = {
                'question': question,
                'choices': choices,
            }
    else:
        context = {}

    return render(request, f'quiz/{filename}', context)


def quiz_result(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    participants = quiz.get_participants()
    result_list = []
    for participant in participants:
        participant_result = quiz.get_score(participant['user__id'])
        participant_result['id'] = participant['user__id']
        participant_result['name'] = participant['user__first_name']
        participant_result['username'] = participant['user__username']
        result_list.append(participant_result)
    paginator = Paginator(result_list, 5)
    page = request.GET.get('page')
    results = paginator.get_page(page)

    return render(request, 'quiz/results.html', {'quiz': quiz, 'results': results})
