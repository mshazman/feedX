from django.urls import path
from . import views as quiz_views

name = 'quiz'
urlpatterns = [
    path('create/',quiz_views.CreateQuizView.as_view(),name='create-quiz'),
    path('generate_id/',quiz_views.generate_id,name='create-id')
]