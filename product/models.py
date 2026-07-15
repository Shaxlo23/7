from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100,blank=True,null=False)

    price = models.PositiveIntegerField(default=0)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    created_date = models.DateField()
    updated_at = models.DateField()