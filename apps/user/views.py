import django.urls
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from apps.user.models import UserModel
from apps.user.serializers import UserSerializers


class CreateUserApiView(CreateAPIView):
    serializer_class = UserSerializers


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroyUserAPIView(RetrieveUpdateDestroyAPIView):
    http_method_names = ("patch", 'delete')
    serializer_class = UserSerializers
    permission_classes: tuple[type[IsAuthenticated]] = (IsAuthenticated,)

    def get_object(self):
        return UserModel.objects.get(pk=self.request.user.pk)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GetMeUser(RetrieveAPIView):
    serializer_class = UserSerializers
    permission_classes: tuple[type[IsAuthenticated]] = (IsAuthenticated,)

    def get_object(self):
        return UserModel.objects.get(pk=self.request.user.pk)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
