from django.urls import path
from albums import views as album_views

urlpatterns = [
    path('', album_views.album_list, name='album_list'),
]