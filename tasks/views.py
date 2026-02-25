from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    # Отримуємо список задач, що належать поточному користувачу,
    # відсортований за дедлайном
    tasks = Task.objects.filter(user=request.user).order_by('deadline')

    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks}
    )


@login_required
def task_create(request):
    # Створення нової задачі
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            # Не зберігаємо одразу, щоб додати користувача
            task = form.save(commit=False)
            task.user = request.user  # Прив’язуємо задачу до поточного користувача
            task.save()

            return redirect('task_list')
    else:
        # Порожня форма для створення задачі
        form = TaskForm()

    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
    )