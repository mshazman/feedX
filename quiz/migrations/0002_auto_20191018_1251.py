# Generated by Django 2.2.6 on 2019-10-18 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question',
            new_name='ques',
        ),
        migrations.RenameField(
            model_name='answersubmission',
            old_name='question',
            new_name='ques',
        ),
        migrations.RenameField(
            model_name='questionchoice',
            old_name='question',
            new_name='ques',
        ),
    ]