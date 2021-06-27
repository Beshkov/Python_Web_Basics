from django.contrib import admin
from django.urls import path

from notes.users_notes.views import index, add_note, delete_note, edit_note, note_details

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', note_details, name='note details'),
]
