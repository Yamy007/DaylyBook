from django.db import models

from apps.user.models import UserModel
from core.models import CoreModel


class TodoModel(CoreModel):
    class Meta:
        db_table = 'todo'
    title = models.CharField(max_length=128)
    owner = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name='todo')
    color = models.CharField(max_length=25)
    is_archive = models.BooleanField(default=False)


class TodoItemModel(models.Model):
    class Meta:
        db_table = 'todo_item'
    title = models.CharField(max_length=64)
    todo = models.ForeignKey(
        TodoModel, on_delete=models.CASCADE, related_name='item')
    is_done = models.BooleanField(default=False)
    color = models.CharField(max_length=25)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
