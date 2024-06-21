from django.db import models

class Article(models.Model):
    judul = models.CharField(max_length = 200)
    penulis = models.CharField(max_length = 100)
    abstrak = models.TextField()
    publish_date = models.DateField()
    
    
    def __str__(self):
        return self.judul