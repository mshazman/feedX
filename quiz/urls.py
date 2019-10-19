from django.urls import path
from . import views as quiz_views

name = 'quiz'
urlpatterns = [
    path('create/',quiz_views.CreateQuizView.as_view(),name='create-quiz'),
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
    path('event/<str:id>/',quiz_views.event,name='event'),
    path('answer/',quiz_views.answerForm,name='answer'),
    path('new/',quiz_views.new_quiz,name="new-quiz")

]