import rest_framework
from rest_framework import status
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.note.models import NoteModel
from apps.note.serializers import NoteSerializer
from apps.user.models import UserModel


class CreateNoteApiView(CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return UserModel(pk=self.request.user.pk)

    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializers = NoteSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save(owner=user)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyNoteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return NoteModel.objects.filter(pk=self.kwargs.get('pk')).filter(owner=UserModel.objects.get(pk=self.request.user.pk)).first()


class GetAllNote(GenericAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, *args, **kwargs):
        user_pk = self.request.user.pk
        user = UserModel.objects.get(pk=user_pk)
        notes = NoteModel.objects.filter(owner=user)
        serializers = NoteSerializer(notes, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
