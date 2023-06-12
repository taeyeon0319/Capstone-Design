from django.db import models

# Create your models here.
class Menu(models.Model):
    CATEGORY = (
        ('오넛지', '오넛지'),
        ('카츠', '카츠'),
        ('더푸리', '더푸리'),

    )
    name = models.CharField('메뉴명', max_length=250, unique=True) #메뉴명
    price = models.IntegerField() #가격
    category = models.CharField(max_length=5, choices=CATEGORY) #카테고리
    image = models.ImageField(upload_to="menu/") #음식이미지


class Cart(models.Model):
    name = models.CharField(max_length=250) #메뉴명
    price = models.IntegerField() #가격
    image = models.TextField() #음식이미지
