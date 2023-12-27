from django import forms
from .models import Comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'date', 'author', 'article']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
        }
