import rest_framework
from rest_framework import status
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.todo.models import TodoItemModel, TodoModel
from apps.todo.serilaizers import TodoItemSerializer, TodoSerializer
from apps.user.models import UserModel


class CreateTodoApiView(CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, *args, **kwargs):
        owner = UserModel.objects.get(pk=self.request.user.pk)
        data = self.request.data
        serializers = TodoSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save(owner=owner)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyTodoAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return TodoModel.objects.filter(pk=self.kwargs.get('pk')).filter(owner=self.request.user.pk).first()


class GetAllTodo(GenericAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return TodoModel.objects.filter(owner=UserModel.objects.get(pk=self.request.user.pk))

    def get(self, *args, **kwargs):
        todo = self.get_object()
        serializers = TodoSerializer(todo)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CreateTodoItemApiView(CreateAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return TodoModel.objects.get(pk=self.kwargs.get('pk'))

    def post(self, *args, **kwargs):
        todo = self.get_object()
        data = self.request.data
        serializers = TodoItemSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save(todo=todo)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyTodoItem(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = (IsAuthenticated,)
