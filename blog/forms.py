from django import forms
from django.forms import ModelForm
from .models import TB_Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = TB_Comment
        fields = ['name', 'email', 'contain']