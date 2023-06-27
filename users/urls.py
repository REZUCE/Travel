# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import (LogoutView, LoginView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'logout/',
        # Прямо в описании обработчика укажем шаблон,
        # который должен применяться для отображения возвращаемой страницы.
        # Да, во view-классах так можно! Как их не полюбить.
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    # все связанное с паролем(регистрация, авторизация и т.п.)
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='users/password_change_done.html'),
         name='password_change_done'
         ),

    path('reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'
         ),
    path('password_change/',
         PasswordChangeView.as_view(
             template_name='users/password_change_form.html'),
         name='password_change_form'
         ),
    path('not-access/', views.not_access, name='not_access'),
    path('profile/', views.profile, name='profile'),

    # path('user/orders/', views.user_orders, name='user_orders')
]
