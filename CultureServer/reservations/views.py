from django.shortcuts import render
from users.models import User
from reservations.models import Reservation
from rest_framework.views import APIView
from rest_framework.response import Response
from reservations.serializers import ReservationSerializer
from rest_framework import status
#이 부분 확인 

class ReservationList(APIView):
	def post(self, request, format=None):
		user = User.objects.get(username=request.query_params.get('username'))
		reservations = Reservation.objects.filter(reserver=user)
		##get 은 하나만, filter 는 여러개 
		serializer = ReservationSerializer(reservations, many=True)
		return Response(serializer.data)
		