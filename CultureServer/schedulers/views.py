from django.shortcuts import render
from schedulers.models import Scheduler
from users.models import User
from schedulers.serializers import SchedulerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import datetime 
import calendar 


#프론트에서 친구 인원을 유동적으로 바꾸면 
#선택한 사람의 데이터를 서버로 보냄
#서버에서 잔체 인원 친구들의 스케줄을 비교해서 빈칸을 찾고 
#그 빈칸에 대한 specificcontent model 을 시간대에 맞는 애들로 필터링해서 가져온 다음 다시 리턴

'''view -> functions
scheduleList - 완료 
get schedule - 완료 
add schedule - 완료 
delete schedule - 완료 
update schedule - 완료 
'''

class ScheduleList(APIView):
	def post(self, request, format=None):
		user = User.objects.get(username=request.data['username'])
		schedules = Scheduler.objects.filter(user=user)
		for schedule in schedules:
			schedule.startDate = self.add_months(schedule.startDate, 0)
			schedule.endDate = self.add_months(schedule.endDate, 0) 
		serializer = SchedulerSerializer(schedules, many=True)
		return Response(serializer.data)
	
	def add_months(self, sourcedate, months):
		month = sourcedate.month - 1 + months
		year = sourcedate.year + month // 12
		month = month % 12 + 1
		day = min(sourcedate.day, calendar.monthrange(year,month)[1])
		hour = sourcedate.hour
		minute = sourcedate.minute
		second = sourcedate.second
		return datetime.datetime(year, month, day, hour, minute, second)


class AddSchedule(APIView):
	def post(self, request, format=None):
		data = request.data
		serializer = SchedulerSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ScheduleDetail(APIView):
	def get_object(self, pk):
		try:
			return Scheduler.objects.get(pk=pk)
		except Scheduler.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		schedule = self.get_object(pk)
		serializer = SchedulerSerializer(schedule)
		return Response(serializer.data)


	def put(self, request, pk, format=None):
		schedule = self.get_object(pk)
		serializer = SchedulerSerializer(schedule, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		schedule = self.get_object(pk)
		schedule.delete()
		return Response(status=status.HTTP_200_OK)