from django.db import models

from apps.user.models import UserModel
from core.models import CoreModel


# Create your models here.
class NoteModel(CoreModel):
    class Meta:
        db_table = 'notes'

    title = models.CharField(max_length=128)
    text = models.TextField()
    owner = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name='note')
    color = models.CharField(max_length=25)
    is_archive = models.BooleanField(default=False)
