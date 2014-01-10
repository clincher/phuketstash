# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailModelBackend(ModelBackend):
    """Бэкэнд для авторизации пользователей при помощи пары email и пароль
    """
    def authenticate(self, email=None, password=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get_by_natural_key(email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
