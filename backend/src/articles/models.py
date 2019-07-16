from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    rv = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.title
