"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    # 127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/
     # path('', views.index),
     # 127.0.0.1:8000/hello/
    path('hello/', views.hello, name='hello_main'), # urls.py의 path('hello/', 에서 ‘hello/’ 앞에는 ‘http://127.0.0.1:8000/’까지가 생략되어있는 것입니다.
     # 127.0.0.1:8000/lotto
    path('lotto/', views.index, name='index'), # lotto > views.py 파일의 index 함수 호출
    path('lotto/new/', views.post, name = "new_lotto"),
    path('lotto/<int:lottokey>/detail', views.detail, name='detail'),
    # int 만 받아서 lottokey라는 이름으로 받아서 넘겨 줄 것이다.
]
