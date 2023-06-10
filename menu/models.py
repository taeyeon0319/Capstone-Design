from django.db import models

# Create your models here.
class Menu(models.Model):
    CATEGORY = (
        ('오넛지', '오넛지'),
        ('카츠', '카츠'),
        ('더푸리', '더푸리'),

    )
    name = models.CharField('메뉴명', max_length=250, unique=True) #메뉴명
    price = models.IntegerField() #메뉴가격
    #info = models.TextField() #메뉴설명
    category = models.CharField(max_length=5, choices=CATEGORY) #카테고리
    #음식이미지 
    image = models.ImageField(upload_to="menu/")

'''
cart 앱 만들고 따로 관리
class Cart(models.Model):
    menu = models.ForeignKey(Menu, models.SET_NULL, blank = True, null=True) #장바구니에 넣는 메뉴 
    count = models.IntegerField() #메뉴 개수
    
'''
class Cart(models.Model):
    name = models.CharField(max_length=250) #메뉴명
    price = models.IntegerField()
    image = models.TextField()
