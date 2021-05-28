from django.shortcuts import render, redirect
from contents.models import Content, SpecificContent
from schedulers.models import Scheduler
from users.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from contents.serializers import ContentSerializer, SpecificContentsSerializer
from schedulers.serializers import SchedulerSerializer
from rest_framework import status
from django.http import Http404
import datetime
from django.db.models import Q


#개인스케줄 비교 - 완료 
#취향 반영 스케줄 - filter, schedule 가져와서 비교, 필터로 가쟈온다음 데이터랑 비교해서 남는거 다 필터 -> 완료 
#specific content 정보 받아오는 것 
#친구랑 스케줄 비교 - 거의 완료...! 이 부분 마무리 하기 
#content search - 완료 
#filter갖고 테마에 따라 보여주는것, object.filter 로직 
#detailview - 완료(?)

#친구랑 스케줄 비교 로직 
#1. 내 스케줄의 schedule list 를 전체 다 불러온다 
#2. 친구 스케줄 schedule list 를 전체 다 불러온다 
#3. 둘의 전체를 하나씩 다 비교한다 
#4. 그 중 둘 다 빈칸인것 (schedule 이 없는 것)들만 비교한다 
#5. serializer 로 결과를 바꾼두ㅏ
#6. return Response(serializer.date...?)

#Q(date__gt=datetime.date.today()) | Q(date__lt=datetime.date.today + datetime.timedelta(days=7))


#나랑 콘텐츠 스케줄 비교로 수정하기 
class CompareIndivdualSchedule(APIView): #개인 스케줄 - 콘텐츠 스케줄 비교 
	def convertToNUM(self, time):
		if(time.hour == 0):
			return (24 * 60 + time.minute) / 30	
		return (time.hour * 60 + time.minute) / 30

	def convertToTime(self, number):
		datetime(hour=(number * 30 / 60), minute=(number * 30 % 60))
		return datetime 


	def getBlank(self, user, date):
		time_set = set([])
		total_set = set(list(range(48)))
		schedules = Scheduler.objects.filter(user=user, startDate=date)
		for schedule in schedules:
			start_num = self.convertToNUM(schedule.startDate)
			end_num = self.convertToNUM(schedule.endDate)
			for i in range(int(start_num), int(end_num)):
				time_set.add(i)
		print("blank: ", total_set - time_set)

		return total_set - time_set


	def post(self, request, format=None): ##data user pk[1, 2, 3]
		filtered_contents = []
		dates = []
		for i in range(7):
			dates.append(datetime.datetime.today() + datetime.timedelta(days=i))

		for date in dates:
			print(date)
			u = User.objects.get(pk=request.data["data"])
			print(u)
			result = self.getBlank(u, date)
			print("result: ", result)
			
			contents = SpecificContent.objects.filter(date=date)
			for content in contents:
				start_num = self.convertToNUM(content.start_time)
				end_num = self.convertToNUM(content.end_time)
				running = set(list(range(int(start_num), int(end_num))))
				print("running: ", running)
				if (result & running) == running:
					filtered_contents.append(content)

		serializer = SpecificContentsSerializer(filtered_contents, many=True)
		return Response(serializer.data)


class CompareSchedule(APIView): #개인 스케줄 & 친구 스케줄 & 콘텐츠 스케줄 비교
	def convertToNUM(self, time):
		if(time.hour == 0):
			return (24 * 60 + time.minute) / 30	
		return (time.hour * 60 + time.minute) / 30

	def convertToTime(self, number):
		datetime(hour=(number * 30 / 60), minute=(number * 30 % 60))
		return datetime 


	def getBlank(self, user, date):
		time_set = set([])
		total_set = set(list(range(48)))
		schedules = Scheduler.objects.filter(user=user, startDate=date)
		for schedule in schedules:
			start_num = self.convertToNUM(schedule.startDate)
			end_num = self.convertToNUM(schedule.endDate)
			for i in range(int(start_num), int(end_num)):
				time_set.add(i)
		print("blank: ", total_set - time_set)

		return total_set - time_set


	def post(self, request, format=None): ##data user pk[1, 2, 3]
		filtered_contents = []
		dates = []
		for i in range(7):
			dates.append(datetime.date.today() + datetime.timedelta(days=i))

		for date in dates:
			set_array = []
			print(date)
			for i in request.data["data"]:
				u = User.objects.get(pk=i)
				print(u)
				set_array.append(self.getBlank(u, date))
			result = set_array[0]
			for _set in set_array:
				result = _set & result
			
			print("result: ", result)
			

			contents = SpecificContent.objects.filter(date=date)
			for content in contents:
				start_num = self.convertToNUM(content.start_time)
				end_num = self.convertToNUM(content.end_time)
				running = set(list(range(int(start_num), int(end_num))))
				print("running: ", running)
				if (result & running) == running:
					filtered_contents.append(content)

		serializer = SpecificContentsSerializer(filtered_contents, many=True)
		return Response(serializer.data)
	


class ContentList(APIView):
	permission_classes = [AllowAny]
	
	def get(self, request, format=None):
		contents = Content.objects.all() 
		##데이터베이스(엑셀 테이블)에서 데이터를 가져온 것. 
		## queryset이라는 형태로 저장이 되는데 이건 API 상태가 아니라서 
		serializer = ContentSerializer(contents, many=True)
		##serializer 가 query set 을 API 형태로 만들어줌
		return Response(serializer.data)
		##response 자체가 API 가 되는 것

class AddContent(APIView):
	def post(self, request, format=None):
		data = request.data
		serializer = ContentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		##serializer는 json api로 날라온걸 query set 으로 바꿔줄때도 쓰임
		##save: 함수안에 create가 이미 들어있어서 데이터베이스에 자동으로 저장됨
		else:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#filter by cateogry 확인 
class getContentByGenre(APIView):
	def post(self, request, format=None):
		contents = Content.objects.filter(genre=request.data["genre"])
		serializer = ContentSerializer(contents, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

		
class getContentByPreference(APIView):
	def post(self, request, format=None):
		user = User.objects.get(pk=request.data["user"])
		contents = Content.objects.filter((Q(preference_one=user.preference_one) | Q(preference_two=user.preference_two) | Q(preference_one=user.preference_two) | Q(preference_two=user.preference_one)) & Q(genre=user.genre))
		serializer = ContentSerializer(contents, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class SearchContent(APIView):
	permission_classes = [AllowAny]

	def get(self, request, format=None):
		results = Content.objects.filter(title__icontains=request.GET['text'])
		serializer = ContentSerializer(results, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class ContentDetail(APIView):
	def get_object(self, pk):
		try:
			return Content.objects.get(pk=pk)
		except Content.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		content = self.get_object(pk)
		serializer = ContentSerializer(content)
		return Response(serializer.data)