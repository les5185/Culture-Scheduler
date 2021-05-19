from django.shortcuts import render, redirect
from users.models import User, Friend
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer, UserSerializerWithToken, FriendSerializer


# Create your views here.

#로그인 
#회원가입 
#프론트에서 폼으로 데이터 넘어오고 회원가입은 취향/생일 등 저장
# 친구 username 및 email 로 검색 
#친구 추가 - username 혹은 email 로 추가 

@api_view(['GET'])
def current_user(request):
	"""
	Determine the current user by their token, and return their data
	"""

	serializer = UserSerializer(request.user)
	return Response(serializer.data)

class UserList(APIView):
	"""
	create a new user. It's called 'UserList' because normally we'd have a get method here too, for retrieving a list all User object
	"""

	permission_classes = (permissions.AllowAny,)

	def post(self, request, format=None):
		serializer = UserSerializerWithToken(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FriendList(APIView):
	def get(self, request, format=None):
		friends = Friend.objects.all()
		serializer = FriendSerializer(friends, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, format=None):
		friends = Friend.objects.all()
		serializer = FriendSerializer(friends, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class AddFriend(APIView):
	def post(self, request, format=None):
		try:
			add_friend = User.objects.get(username=request.data["friend"])
			current_user = User.objects.get(username=request.data["user"])
			friend = Friend.objects.get(current_user=current_user, friend=add_friend)
			return Response(status=status.HTTP_302_FOUND)
		except Friend.DoesNotExist:
			serializer = FriendSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		