from django.db import models

# Create your models here.
class Menu(models.Model):
    CATEGORY = (
        ('버거', '버거'),
        ('사이드', '사이드'),
        ('디저트', '디저트'),
        ('음료', '음료'),

    )
    name = models.CharField('메뉴명', max_length=250, unique=True) #메뉴명
    price = models.IntegerField() #메뉴가격
    info = models.TextField() #메뉴설명
    category = models.CharField(max_length=5, choices=CATEGORY) #카테고리
    #음식이미지 image = models.ImageField(upload_to="", blank=True, null=True)

'''
cart 앱 만들고 따로 관리
class Cart(models.Model):
    SS_CHOICE = (
        ('단품', '단품'),
        ('세트', '세트'),
    )
    menu = models.ForeignKey(Menu, models.SET_NULL, blank = True, null=True) #장바구니에 넣는 메뉴 
    ss_choice = models.CharField(max_length=2, choices = SS_CHOICE) #단품세트 선택
    count = models.IntegerField() #메뉴 개수
    
'''

