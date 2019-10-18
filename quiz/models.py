import secrets
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Quiz(models.Model):

    quiz_id = models.CharField(max_length=50,primary_key=True,null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=50,null=False)
    description = models.TextField(max_length=200,blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_live = models.BooleanField(default=False)

class QuestionType(models.Model):
    name = models.CharField(max_length=30)

class Question(models.Model):
   quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
   ques_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
   ques_id = models.CharField(max_length=50,primary_key=True,null=False)
   ques_text = models.CharField(max_length=30,null=False)
   timestamp = models.DateTimeField(default=timezone.now)

class QuestionChoice(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   choice_id = models.CharField(max_length=50, primary_key=True, null=False)
   choice_text = models.CharField(max_length=30,null=False)

class Answer(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   answer = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)

class AnswerSubmission(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   sub_answer = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, null=True)
   text_answer = models.CharField(max_length=150, null=True)
   is_right = models.BooleanField(null=True)