from rest_framework import serializers
from quiz.models import *
from django.contrib.auth.models import User


class ChoiceSerializer(serializers.ModelSerializer):
    choice_id = serializers.CharField()

    class Meta:
        model = QuestionChoice
        fields = ['choice_id', 'ques', 'choice_text']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['ques', 'answer']


class QuestionSerializer(serializers.ModelSerializer):
    ques_id = serializers.CharField()
    choices = ChoiceSerializer(read_only=True, many=True)
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['ques_type','ques_id', 'ques_text', 'timestamp', 'quiz', 'choices', 'answers']
        read_only_fields = ['timestamp']


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerSubmission
        fields = ['user', 'ques', 'sub_answer', 'text_answer', 'is_right', 'quiz']
        read_only_fields = ['is_right']


class QuizSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    quiz_id = serializers.CharField(read_only=True)
    questions = QuestionSerializer(read_only=True, many=True)
    submissions = SubmissionSerializer(read_only=True, many=True)

    class Meta:
        model = Quiz
        fields = ['title', 'owner', 'description', 'quiz_id', 'questions', 'submissions']


