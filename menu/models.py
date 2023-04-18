from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()
    price = models.CharField(max_length=20)
    #count
    #음식이미지 image = 