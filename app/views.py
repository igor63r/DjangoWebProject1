"""
Definition of views.
"""

from django.shortcuts import render, redirect 
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def registration(request):
    """Renders the registration page."""
      
    if request.method == "POST":                        # после отправки формы
        regform = UserCreationForm(request.POST) 
        if regform.is_valid():                           #валидация полей формы
            reg_f = regform.save(commit=False)   # не сохраняем данные формы
            reg_f.is_staff = False  # запрещен вход в административный раздел
            reg_f.is_active = True                       # активный пользователь
            reg_f.is_superuser = False            # не является суперпользователем
            reg_f.date_joined = datetime.now()           # дата регистрации 
            reg_f.last_login = datetime.now()        # дата последней авторизации
            
            reg_f.save()                                 # сохраняем изменения после добавления данных (добавление пользователя в БД пользователей) 
       
            return redirect('home')                     # переадресация на главную страницу после регистрации
    else:                                           
        regform = UserCreationForm()                     # создание объекта формы для ввода данных нового пользователя
   
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {                                           
            
            'regform': regform,           # передача формы в шаблон веб-страницы
            
            'year':datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
