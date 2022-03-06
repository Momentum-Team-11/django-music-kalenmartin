from django.urls import path, include
from albums import views as albums_views

urlpatterns = [
    path('', albums_views.album_list, name='album_list'),
    path('albums/<int:pk>/', albums_views.album_detail, name="album_detail"),
    path('albums/add/', albums_views.album_add, name='album_add'),
    # path('albums/<int:pk>/album/', albums_views.album_add, name='album_add'),
]



# from django.contrib import admin
# from django.conf import settings
# from django.urls import path
# from albums import views as albums_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', albums_views.album_list, name='album_list'),
#     path('albums/<int:pk>/', albums_views.album_detail, name="album_detail"),
#     path('albums/album_add', albums_views.album_add, name='album_add'),
#     ]