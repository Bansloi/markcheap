from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


from accounts.manager import UserManager
from django.contrib.auth.models import PermissionsMixin
import datetime

# Create your models here.


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    password = models.CharField(max_length=100)
    last_login = datetime.datetime.now()
    date_joined = datetime.datetime.now()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "password"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False
