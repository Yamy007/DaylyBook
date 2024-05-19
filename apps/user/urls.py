
from django.urls import path

from .views import (CreateUserApiView, GetMeUser,
                    RetrieveUpdateDestroyUserAPIView)

urlpatterns = [
    path('create', CreateUserApiView.as_view(), name="create_user"),
    path('update', RetrieveUpdateDestroyUserAPIView.as_view(),
         name="get , update or delete"),
    path('me', GetMeUser.as_view(), name="get me"),
]
