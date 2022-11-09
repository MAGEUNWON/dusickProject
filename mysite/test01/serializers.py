from rest_framework.serializers import ModelSerializer
from .models import Kosdak000250M

#django_framework는  RESTful한 API를 쉽게 만들 수 있도록 해줌
#rest_framework 안먹히면 인터프리터 설정 확인해보기 (글로벌로 하면 됨)

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = Kosdak000250M #모델 설정
        fields = '__all__' #필드 설정


# Serializer란 queryset과 모델 인스턴스와 같은 복잡한 데이터를(DB에서 불러온 데이터를) json,xml 또는 다른 콘텐츠 유형으로 쉽게 변환할 수 있음. 데이터 직렬화를 의미. 