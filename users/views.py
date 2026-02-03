from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    """
    В'юшка для реєстрації нового користувача.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Одразу логінимо юзера після реєстрації (необов'язково, але зручно)
            # login(request, user) 
            # За завданням треба редірект на логін:
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

def home(request):
    """Проста головна сторінка"""
    return render(request, 'home.html')