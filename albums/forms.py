# from socket import fromshare
from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'created_at',
        ]

# class ArtistForm(forms.ModelForm):
#     class Meta:
#         model = Artist
#         fields = ['artist']