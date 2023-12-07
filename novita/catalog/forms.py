from django import forms
from catalog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'name', 'category']

        labels = {
            'title': 'Содержание',
            'name': 'Заголовок',
            'category': 'Категория'
        }

        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-text', 'cols': 80, 'rows': 15}),
        }


class RegisterUserForm(forms.ModelForm): # регистрация
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }