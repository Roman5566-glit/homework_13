from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Створюємо клас налаштувань для адмінки
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Додаємо наші нові поля у відображення в адмінці
    # fieldsets - це групування полів при редагуванні користувача
    fieldsets = UserAdmin.fieldsets + (
        ('Додаткова інформація', {'fields': ('bio', 'birth_date')}),
    )
    # add_fieldsets - це поля при створенні користувача
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Додаткова інформація', {'fields': ('bio', 'birth_date')}),
    )

# Реєструємо
admin.site.register(CustomUser, CustomUserAdmin)