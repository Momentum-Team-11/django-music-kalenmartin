from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all()
    
    return render(request, "album_list.html",
        {"albums": albums})

def album_detail(request, pk):
    album  = get_object_or_404(Album, pk=pk)
    form = AlbumForm()
    return render (request,"albums/album_detail.html",
        {"album":album, "pk":pk, "form":form},
    )

def album_add(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='album_add')

    return render(request, "albums/album_add.html",
        {"form":form}
    )