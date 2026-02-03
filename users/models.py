from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Кастомна модель користувача.
    Наслідується від AbstractUser, тому має всі стандартні поля 
    (username, email, password, first_name, last_name).
    """
    # Додаткове поле, як вимагає завдання
    bio = models.TextField(verbose_name="Про себе", blank=True, null=True)
    
    # Можна додати ще дату народження або телефон, наприклад:
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата народження")

    def __str__(self):
        return self.username