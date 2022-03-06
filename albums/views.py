from django.shortcuts import render
from .models import Album


def album_list(request):
    albums = Album.objects.all()
    
    return render(request, "album_list.html",
        {"albums": albums})

