from django.shortcuts import render
from .models import Album, Artist
from .forms import AlbumForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def album_list(request):
    album = Album.objects.all()
    # artists = Artist.objects.all()
    return render(request, "albums/album_list.html",
        {"albums": album})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm()
    return render (
        request,
        "albums/album_detail.html",
        {"album": album, "pk":pk, "form":form},)
