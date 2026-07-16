from django.db import models

# Create your models here.

class Library(models.Model):
    title = models.CharField(max_length=100,blank=True,null=False)

    author = models.CharField(max_length=50,null=False,blank=False)

    description = models.TextField()

    genre = models.CharField(max_length=50,null=False,blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField()