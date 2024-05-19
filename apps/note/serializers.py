from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.user.serializers import UserSerializers

from .models import NoteModel


class NoteSerializer(ModelSerializer):
    owner = UserSerializers(read_only=True)

    class Meta:
        model = NoteModel
        fields = ('id', 'title', 'text', 'owner', 'color', 'is_archive',)
