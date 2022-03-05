from socket import fromshare
from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        field = ['title']
        field = ['artist']
        field = ['created_at']

# class ArtistForm(forms.ModelForm):
#     class Meta:
#         model = Artist
#         fields = ['artist']