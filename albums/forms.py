# from socket import fromshare
from django import forms
from .models import album
# from attr import fields

class AlbumForm(forms.ModelForm):
    class Meta:
        model = album
        fields = ['title','artist', 'created_at']

# class ArtistForm(forms.ModelForm):
#     class Meta:
#         model = Artist
#         fields = ['artist']