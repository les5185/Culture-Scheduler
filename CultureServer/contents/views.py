from django.shortcuts import render
from contents.models import Content
from rest_framework.views import APIView
from rest_framework.response import Response
from contents.serializers import ContentSerializer
from rest_framework import status
#이 부분 확인 

class ContentList(APIView):
	def get(self, request, format=None):
		contents = Content.objects.all() 
		##데이터베이스(엑셀 테이블)에서 데이터를 가져온 것. 
		## queryset이라는 형태로 저장이 되는데 이건 API 상태가 아니라서 
		serializer = ContentSerializer(contents, many=True)
		##serializer 가 query set 을 API 형태로 만들어준다.
		return Response(serializer.data)
		##response 자체가 API 가 되는 것

class AddContent(APIView):
	def post(self, request, format=None):
		data = request.data
		serializer = ContentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		##serializer는 json api로 날라온걸 query set 으로 바꿔줄때도 쓰인다
		##save 란 함수안에 create가 이미 들어있어서 데이터베이스에 자동으로 저장됨
		else:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)