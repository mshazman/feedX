from django.urls import path
from . import views as quiz_views

name = 'quiz'
urlpatterns = [
    path('api/quiz/', quiz_views.ListQuizView.as_view()),
    path('api/quiz/<pk>/', quiz_views.DetailQuizView.as_view()),
    path('api/questions/', quiz_views.ListQusetionView.as_view()),
    path('api/questions/<pk>/', quiz_views.DetailQuestionView.as_view()),
    path('api/choices/', quiz_views.ListChoiceView.as_view()),
    path('api/choices/<pk>', quiz_views.ListChoiceView.as_view()),
    path('api/answers/', quiz_views.ListAnswerView.as_view()),
    path('api/answers/<pk>', quiz_views.DetailAnswerView.as_view()),
    path('api/submission', quiz_views.ListSubmissionView.as_view()),
    path('api/submission/<pk>', quiz_views.DetailSubmissionView.as_view()),
    path('generate_id/',quiz_views.generate_id,name='create-id'),
    path('event/<str:id>/',quiz_views.take_quiz,name='event'),
    path('answer/',quiz_views.answerForm,name='answer'),
    path('new/',quiz_views.new_quiz,name="new-quiz"),
    # path('take/quiz/<str:id>',quiz_views.take_quiz, name="take-quiz"),
    path('template/render/<str:filename>',quiz_views.quiz_template_render, name='template-render'),
    path('result/<str:quiz_id>/', quiz_views.quiz_result, name='result')

]