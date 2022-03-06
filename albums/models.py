from django.db import models
from datetime import datetime



class Album(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=datetime.now)
    
    def __str__(self):
        return self.title

    # def __str__(self):
    #     return self.artist

    # def __str__(self):
    #     return self.created_at
