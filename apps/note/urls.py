from django.urls import path

from .views import (CreateNoteApiView, GetAllNote,
                    RetrieveUpdateDestroyNoteApiView)

urlpatterns = [
    path('create', CreateNoteApiView.as_view(), name='create'),
    path('update', RetrieveUpdateDestroyNoteApiView.as_view(),
         name='retrieve, update, destroy'),
    path('getAll', GetAllNote.as_view(), name='get_all'),
]
