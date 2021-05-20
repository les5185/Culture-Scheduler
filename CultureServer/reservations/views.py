from django.shortcuts import render
from users.models import User
from reservations.models import Reservation
from rest_framework.views import APIView
from rest_framework.response import Response
from reservations.serializers import ReservationSerializer
from rest_framework import status
from django.http import Http404

class ReservationList(APIView):
	def post(self, request, format=None):
		user = User.objects.get(username=request.data['username'])
		reservations = Reservation.objects.filter(reserver=user)
		##get 은 하나만, filter 는 여러개 
		serializer = ReservationSerializer(reservations, many=True)
		return Response(serializer.data)


class AddReservation(APIView):
	def post(self, request, format=None):
		data = request.data
		serializer = ReservationSerializer(data=data)
		companions = data['companion']
		##validate을 할 때 serializer의 모든 field를 확인하는데 pop을 하면 companion 이 없어지니까 validation_error가 자꾸 뜬것....
		if serializer.is_valid():
			reservation = serializer.save()
			for companion in companions:
			##대신 여기서 객체로 넣어주는게 맞음 
				c = User.objects.get(pk=companion)
				reservation.companion.add(c)
			reservation.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		

class ReservationDetail(APIView):
	def get_object(self, pk):
		try:
			return Reservation.objects.get(pk=pk)
		except Reservation.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		reservation = self.get_object(pk)
		serializer = ReservationSerializer(reservation)
		return Response(serializer.data)
	
	def delete(self, request, pk, format=None):
		reservation = self.get_object(pk)
		reservation.delete()
		return Response(status=status.HTTP_200_OK)


'''add할때 친구를 추가해서 넘겨줘야하고 delete 추가
#프론트에서 시간, 날짜 등 선택해서 보내주면 그걸 addreservation 에서 돌리기 
#프론트에서 정보 넘겨주면 - 애드 로직 
#delete reservation 
#같이 갈 친구 추가 
'''
		