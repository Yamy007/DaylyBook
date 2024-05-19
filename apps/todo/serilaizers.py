from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.todo.models import TodoItemModel, TodoModel
from apps.user.serializers import UserSerializers


class TodoItemSerializer(ModelSerializer):

    class Meta:
        model = TodoItemModel
        fields = ('id', 'title',  'date_start', 'date_end')


class TodoSerializer(ModelSerializer):
    owner = UserSerializers(read_only=True)
    item = TodoItemSerializer(read_only=True, many=True)

    class Meta:
        model = TodoModel
        fields = ('id', 'owner', 'color', 'is_archive', 'item')
