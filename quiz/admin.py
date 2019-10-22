from django.contrib import admin
from .models import Quiz, Question, QuestionChoice, QuestionType, Answer, AnswerSubmission

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(QuestionType)
admin.site.register(AnswerSubmission)
admin.site.register(Answer)
