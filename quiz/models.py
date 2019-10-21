from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Quiz(models.Model):

    quiz_id = models.CharField(max_length=50,primary_key=True,null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=50,null=False)
    description = models.TextField(max_length=200,blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_live = models.BooleanField(default=False)

    def is_participant(self,user_id):
        submission_count = self.submission.values('sub_answer').filter(user=user_id).count()
        if submission_count is 0:
            return False
        else:
            return True

    def check_answer(self, ques, user):
        ques_type = ques.ques_type.id
        submissions = self.submission.filter(ques=ques, user=user)
        submitted_answer_ids = []
        for submission in submissions:
            submitted_answer_ids.append(submission.sub_answer.choice_id)

        if submissions:
            if ques_type == 1:
                return "No result for text question"
            elif ques_type == 2 or ques_type == 3 or ques_type == 4:
                answers = ques.answers.all()
                correct_answer_ids = []
                for answer in answers:
                    correct_answer_ids.append(answer.answer.choice_id)

                if correct_answer_ids == submitted_answer_ids:
                    return "Right"
                else:
                    return "Wrong"
        else:
            return "Answer not sumbitted"


class QuestionType(models.Model):
    name = models.CharField(max_length=30)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    ques_type = models.ForeignKey(QuestionType,related_name='questions', on_delete=models.CASCADE)
    ques_id = models.CharField(max_length=50,primary_key=True,null=False)
    ques_text = models.CharField(max_length=150)
    timestamp = models.DateTimeField(default=timezone.now)


class QuestionChoice(models.Model):
    ques = models.ForeignKey(Question,related_name='choices', on_delete=models.CASCADE)
    choice_id = models.CharField(max_length=50, primary_key=True, null=False)
    choice_text = models.CharField(max_length=50)


class Answer(models.Model):
    ques = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.ForeignKey(QuestionChoice, related_name='answers', on_delete=models.CASCADE)


class AnswerSubmission(models.Model):
    user = models.ForeignKey(User,related_name='submission', on_delete=models.CASCADE)
    ques = models.ForeignKey(Question,related_name='submission', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,related_name='submission', on_delete=models.CASCADE)
    sub_answer = models.ForeignKey(QuestionChoice, related_name='submission', on_delete=models.CASCADE, null=True)
    text_answer = models.CharField(max_length=150, null=True)
    is_right = models.BooleanField(null=True)



