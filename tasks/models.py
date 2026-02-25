from django.db import models
from django.conf import settings  # Використовуємо налаштування для зв’язку з кастомним користувачем


class Task(models.Model):
    # Назва задачі
    title = models.CharField(
        max_length=200,
        verbose_name="Назва задачі"
    )

    # Опис задачі (необов’язкове поле)
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Опис"
    )

    # Дата та час дедлайну
    deadline = models.DateTimeField(
        verbose_name="Дедлайн"
    )

    # Статус виконання задачі
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Виконано"
    )

    # Зв’язок «один користувач — багато задач»
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name="Користувач"
    )

    def __str__(self):
        # Текстове представлення задачі
        return self.title