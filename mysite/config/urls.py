"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
#라우터 추가할거니까 import include를 반드시 포함시켜야 함. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('test01.urls')),
]
# test01 폴더에 있는 urls를 추가해줌. 
# urlpatterns 변수에 지정되어 있는 URL 리스트 를 검사함.
# 위에서부터 순서대로 URL 리스트의 내용을 검사하면서 URL 패턴이 매치되면 검사를 종료. 여기서 끝나면 test01 url.py로 넘어가는 것.