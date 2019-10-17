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

    # def generate_id(self):
    #     return str('q'+secrets.token_hex(8))