from django.urls import path
from . import views

urlpatterns = [
    path('test01datas/', views.getTestDatas, name="test01datas"),
    path('test01datas/<str:day>', views.getTestDatas, name="test01data")
]

#test01datas/ 가 url이됨. getTestDatas는 serializers.py 에 있는 함수(뷰)