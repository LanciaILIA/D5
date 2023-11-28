from django import forms
# from datetime import date

class PostForm(forms.Form):
    name = forms.CharField(label='Название статьи')
    # title = forms.TextField(label='Текст статьи')
