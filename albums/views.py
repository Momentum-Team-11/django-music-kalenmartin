from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all()
    
    return render(request, "album_list.html",
        {"albums": albums})

def album_detail(request, pk):
    album  = get_object_or_404(Album, pk=pk)
    return render (request,"album_detail.html",
        {"album":album}
    )

def album_add(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='album_list')

    return render(request, "album_add.html",
        {"form":form}
    )

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='album_list')

    return render(request, "album_edit.html",
        {"form": form, "album": album})