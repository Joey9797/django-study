from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image_description' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_public' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
