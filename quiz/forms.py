import secrets
from django.forms import ModelForm
from .models import Quiz

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['title','description']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'Quiz Name'})
        self.fields['description'].widget.attrs.update({'class':'form-control','placeholder':'Describe your quiz.','rows':'3'})

    def generate_id(self):
        return str('q'+secrets.token_hex(8))
