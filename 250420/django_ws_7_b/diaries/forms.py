from django import forms
from .models import Diary, Comment


class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        fields = ('image', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)