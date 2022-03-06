from django.db import models



class Album(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    created_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    # def __str__(self):
    #     return self.artist

    # def __str__(self):
    #     return self.created_at
