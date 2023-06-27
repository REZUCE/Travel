# Импортируем CreateView, чтобы создать ему наследника
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy
from orders.models import Order
# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm
from django.shortcuts import render



class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('tickets:index_search')
    template_name = 'users/signup.html'


@login_required
def profile(request):
    lastname = request.user.lastname
    patronymic = request.user.patronymic
    name = request.user.name
    mail = request.user.mail
    number = request.user.number

    return render(request, 'users/profile.html', {
        'name': name,
        'lastname': lastname,
        'patronymic': patronymic,
        'mail': mail,
        'number': number
    })


@login_required
def not_access(request):
    return render(request, 'users/f.html')
