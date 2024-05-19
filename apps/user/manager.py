import os
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from django.http import Http404


class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("Fields username must be required")
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault("is_superuser", True)

        if not kwargs.get("is_superuser"):
            raise ValueError("filed is_superuser must be True")

        user = self.create_user(username, password, **kwargs)
        return user
