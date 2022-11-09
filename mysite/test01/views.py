# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Kosdak000250M
from .serializers import TestDataSerializer
# from rest_framework import status 
#post 요청할 때는 status import 함

@api_view(['GET'])
def getTestDatas(request):
    datas = Kosdak000250M.objects.all() #테이블에 있는 데이터 모두 불러오겠다는 의미
    serializer = TestDataSerializer(datas, many = True) 
    return Response(serializer.data)

# 장고에서 뷰는 함수 또는 클래스의 메소드로 작성. 웹 요청을 받고 응답을 반환해줌. 응답은 HTML 데이터 일 수도 있고, 리다이렉션 명령일 수도 있고 404에러 메세지 일 수도 있음. 다양한 형태의 응답 데이터를 만들어내기 위한 로직을 뷰에 작성하는 것.

# @api_view(['GET'])
# def getTestDatas(request, day):
#     datas = Kosdak000250M.objects.get(day=day)
#     serializer = TestDataSerializer(datas, many = False)
#     return Response(serializer.data)





# Create your views here.
