from django.contrib import admin

from .models import Quiz, QuestionType, Question

# Register your models here.

admin.site.register(Quiz)
admin.site.register(QuestionType)
admin.site.register(Question)

