from django.shortcuts import render
from .models import Album

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    # artists = Artist.objects.all()
    return render(request, "album_list.html",
        {"albums": albums})