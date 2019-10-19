from rest_framework import serializers
from quiz.models import *
from django.contrib.auth.models import User
import secrets


class QuizSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    quiz_id = serializers.CharField(read_only=True)
    class Meta:
        model = Quiz
        fields = ['owner', 'title', 'description', 'quiz_id']
        read_only_fields = ['quiz_id', 'owner']


class QuestionSerializer(serializers.ModelSerializer):
    ques_id = serializers.CharField(read_only=True)
    class Meta:
        model = Question
        fields = ['ques_type','ques_id', 'ques_text', 'timestamp', 'quiz']
        read_only_fields = ['ques_id','timestamp']


class ChoiceSerializer(serializers.ModelSerializer):
    choice_id = serializers.CharField(read_only=True)
    class Meta:
        model = QuestionChoice
        fields = ['choice_id', 'ques', 'choice_text']
        read_only_fields = ['choice_id']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['ques', 'answer']


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerSubmission
        fields = ['user', 'ques', 'sub_answer', 'text_answer' 'is_right',]
        read_only_fields = ['user', 'is_right']


class QuizProfileSerilaizer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)
    questions = QuestionSerializer(read_only=True, many=True)
    class Meta:
        model = Quiz
        fields = ['title', 'owner', 'description', 'quiz_id', 'questions']
