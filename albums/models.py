from django.db import models
from datetime import datetime


# class Artist(models.Model):
#     artist = models.CharField(max_length=300)


class Album(models.Model):
    title = models.CharField(max_length=300)
    # artist = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=datetime.now)
