from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Вказуємо поля, які будуть у формі реєстрації
        fields = ('username', 'email', 'bio', 'birth_date')