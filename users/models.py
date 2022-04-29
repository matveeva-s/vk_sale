from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    sys_id = models.IntegerField('Id в sys', unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
