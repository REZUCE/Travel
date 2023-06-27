from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(login=username)
        except User.DoesNotExist:
            return None
        print(user.role_id)
        if user.role_id.pk != 4:

            raise ValidationError("Вы не являетесь клиентом")

        elif user.check_password(password):
            return user
