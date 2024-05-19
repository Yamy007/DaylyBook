from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from apps.user.manager import UserManager
from core.models import CoreModel


# Create your models here.
class UserModel(CoreModel, AbstractBaseUser):
    class Meta:
        db_table = "auth_users"

    username = models.CharField(max_length=22, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='avatar/', blank=True, null=True)
    # only for test all function project
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    objects = UserManager()
