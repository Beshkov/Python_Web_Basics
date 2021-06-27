from django.contrib import admin
from django.urls import path

from notes.profiles.views import profile_page, create_profile, delete_profile

urlpatterns = [
    path('', profile_page, name='profile'),
    path('create_profile/', create_profile, name='create profile'),
    path('delete/', delete_profile, name='delete profile'),
]
