from django.urls import path
from . import views

# шляхи, що обслуговуються додатком tasks
urlpatterns = [
    # список задач користувача
    path('', views.task_list, name='task_list'),
    # форма створення нової задачі
    path('create/', views.task_create, name='task_create'),
]
