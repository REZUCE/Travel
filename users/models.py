from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxLengthValidator
from django.db import models


class Role(models.Model):
    """Модель роли."""

    id_role = models.AutoField(db_column='id_Role', primary_key=True)
    role_name = models.CharField(db_column='Role_Name', max_length=15, unique=True)
    role_activity = models.BooleanField(db_column='Role_Activity')

    class Meta:
        managed = False
        db_table = 'role'


class CustomUserManager(UserManager):
    def _create_user(self, login, password, mail, **extra_fields):
        """
        Создает и сохраняет пользователя с указанным логином и паролем.
        """
        if not login:
            raise ValueError('The Login field must be set')
        if not mail:
            raise ValueError('You have not provided a valid e-mail')

        mail = self.normalize_email(mail)
        user = self.model(login=login, mail=mail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, login=None, password=None, mail=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, password, mail, **extra_fields)

    def create_superuser(self, login=None, password=None, mail=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя с указанным логином и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(login, password, mail, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя."""

    id_user = models.AutoField(db_column='id_User', primary_key=True)
    role_id = models.ForeignKey(Role, on_delete=models.SET_DEFAULT, db_column='Role_id', default=4)

    name = models.CharField(db_column='Name', max_length=15, verbose_name='Имя')
    lastname = models.CharField(
        db_column='LastName', max_length=15, verbose_name='Фамилия')
    patronymic = models.CharField(
        db_column='Patronomic', max_length=15,
        blank=True, null=True, verbose_name='Отчество'
    )
    login = models.CharField(
        db_column='Login', unique=True,
        max_length=25, verbose_name='Логин',
        help_text='Здесь вводится логин.'
    )

    password = models.CharField(db_column='Password', max_length=25,
                                verbose_name='Пароль', validators=[MaxLengthValidator(25)])
    number = models.CharField(db_column='Number', max_length=15,
                              verbose_name='Номер телефона', blank=True, null=True)

    mail = models.EmailField(
        db_column='Mail', max_length=25,
        help_text='Здесь вводится почта.'
    )
    is_active = models.BooleanField(db_column='is_active', default=True)
    is_staff = models.BooleanField(db_column='is_staff', default=False)
    is_superuser = models.BooleanField(db_column='is_superuser', default=False)

    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "login"
    EMAIL_FIELD = 'mail'
    REQUIRED_FIELDS = ['name', 'lastname', 'patronymic', 'mail']

    # отключение функции проверки пароля по хэшу
    def check_password(self, raw_password):
        return self.password == raw_password

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'user'
