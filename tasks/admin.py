from django.contrib import admin
from .models import Task

# Реєстрація моделі Task у адмінці
# (щоб адміністратор міг додавати, редагувати, фільтрувати задачі)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # покажемо основні поля у списку
    list_display = ('title', 'user', 'deadline', 'is_completed')
    # дозволимо фільтрацію за статусом і датою
    list_filter = ('is_completed', 'deadline', 'user')
    # пошук за назвою, описом або іменем користувача
    search_fields = ('title', 'description', 'user__username')
    # сортування за дедлайном за замовчуванням
    ordering = ('deadline',)

