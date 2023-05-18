from django.db import models

# Create your models here.
class Snippet(models.Model):
    Title = models.CharField(max_length=150)
    Code = models.CharField(max_length=150)
    linenos = models.BooleanField(unique=True)
    Language = models.CharField(max_length=100)
    Style= models.CharField(max_length=50)

    def __str__(self):
        return self.Title