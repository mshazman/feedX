from django.urls import path
from . import views as quiz_views

name = 'quiz'
urlpatterns = [
    path('api/quiz/', quiz_views.ListQuizAPI.as_view()),
    path('api/quiz/<pk>/', quiz_views.DetailQuizAPI.as_view()),
    path('api/questions/', quiz_views.ListQusetionAPI.as_view()),
    path('api/questions/<pk>/', quiz_views.DetailQuestionAPI.as_view()),
    path('api/choices/', quiz_views.ListChoiceAPI.as_view()),
    path('api/choices/<pk>', quiz_views.ListChoiceAPI.as_view()),
    path('api/answers/', quiz_views.ListAnswerAPI.as_view()),
    path('api/answers/<pk>', quiz_views.DetailAnswerAPI.as_view()),
    path('api/submission', quiz_views.ListSubmissionAPI.as_view()),
    path('api/submission/<pk>', quiz_views.DetailSubmissionAPI.as_view()),
    path('generate_id/', quiz_views.generate_id, name='create-id'),
    path('event/<str:id>/', quiz_views.take_quiz, name='event'),
    path('answer/', quiz_views.answer_form, name='answer'),
    path('new/', quiz_views.new_quiz, name="new-quiz"),
    path('template/render/<str:filename>', quiz_views.quiz_template_render, name='template-render'),
    path('result/<str:quiz_id>/', quiz_views.quiz_result, name='result')

]
