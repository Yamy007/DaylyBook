import django.db
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.user.models import UserModel


class UserSerializers(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'image',
                  'is_superuser', 'create_at', 'update_at', 'last_login')
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }
        read_only_fields = ('is_superuser', 'image', 'last_login',)
