from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # Вбудовані шляхи для auth (login, logout, password_reset...)
    path('accounts/', include('django.contrib.auth.urls')),
    # Шляхи нашого додатку users
    path('users/', include('users.urls')),
    # Головна сторінка
    path('', home, name='home'),
]