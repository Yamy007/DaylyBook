from django.urls import path

from .views import (CreateTodoApiView, CreateTodoItemApiView, GetAllTodo,
                    RetrieveUpdateDestroyTodoAPIView,
                    RetrieveUpdateDestroyTodoItem)

urlpatterns = [
    path('create', CreateTodoApiView.as_view(), name='create'),
    path('add/item', CreateTodoItemApiView.as_view(), name='add item todo'),
    path('update/item', RetrieveUpdateDestroyTodoItem.as_view(), name='add item todo'),
    path('update', RetrieveUpdateDestroyTodoAPIView.as_view(),
         name='retrieve, update, destroy'),
    path('getAll', GetAllTodo.as_view(), name='get_all'),
]
