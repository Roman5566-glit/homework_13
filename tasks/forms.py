from django import forms
from django.utils import timezone
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        # Модель, з якою працює форма
        model = Task

        # Поля, які будуть відображені у формі
        fields = ['title', 'description', 'deadline', 'is_completed']

        # Налаштування віджетів для полів форми
        widgets = {
            # HTML5 поле вибору дати та часу
            'deadline': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
        }

    def clean_deadline(self):
        """
        Перевірка поля deadline.
        Забороняє встановлювати дедлайн у минулому.
        """
        deadline = self.cleaned_data.get('deadline')

        if deadline and deadline < timezone.now():
            raise forms.ValidationError(
                "Дедлайн не може бути в минулому!"
            )

        return deadline