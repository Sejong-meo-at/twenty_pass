from django import forms
from .models import TwentyPass

class PostForm(forms.ModelForm):

    class Meta:
        model = TwentyPass
        fields = ('title', 'question', 'answer',)
