from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path('noteadd', NoteAdd, name='noteadd'),
    path('', ViewNote, name='noteshow'),
    path('edit/<int:id>', EditNote),
    path('update/<int:id>', UpdateNote),
    path('delete/<int:id>', DestroyNote),
]