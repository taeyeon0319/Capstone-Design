# 동키 키오스크   
## 프로젝트 소개
### 1. donkey 폴더
#### donkey>static
> css, img, js를 관리하는 static 폴더   

### donkey>templates>base.html
> 전체적인 화면 크기와 색깔, html기본 구조를 다뤄 다른 html파일의 base가 되는 파일   

### donkey>urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('menu/', include('menu.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> /admin : admin페이지   
> / : main앱의 url을 가져옴   
> /menu : menu앱의 url을 가져옴   
> static : MEDIA_ROOT에 Media이미지들을 저장함   

### donkey>settings.py
> 프로젝트의 앱 등록, 사용자 등록, 언어/서버시간 설정 등의 프로젝트 내 웹 설정을 담당   

### 2. main 폴더
#### main>templates>main>....html
> 모델이 필요없는 단순 페이지들을 모아둠.   
> 직원호출(employee_call.html), 결제완료(final.html), 메인(mainpage.html), 결제(pay.html)


### main>urls.py
```
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('call/', employee_call, name="employee_call"),
    path('cart/', cart_list, name="cart_list"),
    path('pay/', pay, name="pay"),
    path('final/', final, name="final"),
]
```

> / : 메인페이지 url   
> /call : 직원호출 페이지 url   
> /cart : 장바구니 페이지 url   
> /pay : 결제 페이지 url  
> /final : 결제완료 페이지 url

### main>views.py
> templates>main에 있는 모든 html페이지들을 url에 연결해줌

### 3. media 폴더
#### media>cart
> cart모델의 이미지를 저장하는 폴더

#### media>menu
> menu모델의 이미지를 저장하는 폴더


### 4. menu 폴더
#### menu>templates>menu>cart_list.html
> cart모델의 모든 데이터를 보여주고 장바구니 데이터 삭제가 가능한 페이지

#### menu>templates>menu>menu_list.html
> menu모델의 모든 데이터를 보여주고 cart모델의 Read와 Delete가 가능한 페이지

### menu>models.py
>  menu모델 : name, price, category, image를 속성으로 갖는다.   
>  cart모델링 : name, price, image를 속성으로 갖는다.

### menu>urls.py
```
urlpatterns = [
    path('', menu, name="menu"),
    path('cart_push', cart_push, name="cart_push"),
    path('delete', cart_delete, name="cart_delete"),
    path('delete/<int:id>', cart_delete_each, name="delete"),
    path('delete2/<int:id>', cart_delete_each2, name="delete2"),
]
```

> /menu : 메뉴페이지 url   
> /menu/cart_push : 장바구니에 데이터 CREATE을 진행함   
> /menu/delete : 장바구니의 모든 데이터 DELETE을 진행함   
> /menu/delete/<int:id> : 장바구니의 해당 id의 데이터 DELETE을 진행함. 

### menu>views.py
> menu : menu모델 READ   
> cart_push : cart모델 CREATE   
> cart_delete : cart모델 DELETE   
> cart_list : cart모델 READ   
> cart_delete_each(request, id) : 해당 id의 cart모델 DELETE   
