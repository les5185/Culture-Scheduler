from django.shortcuts import render
from schedulers.models import Scheduler
from users.models import User
from schedulers.serializers import SchedulerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


#프론트에서 친구 인원을 유동적으로 바꾸면 
#선택한 사람의 데이터를 서버로 보낸다
#서버에서 잔체 인원 친구들의 스케줄을 비교해서 빈칸을 찾고 
#그 빈칸에 대한 specificcontent model 을 시간대에 맞는 애들로 필터링해서 가져온다음
#다시 리턴을 해준다 

'''자기 모든 스케줄 불러오는 view
같이 가기 추천 view 
add schedule 
delete schedule 
update schedule 

'''

class ScheduleList(APIView):
	def post(self, request, format=None):
		user = User.objects.get(username=request.data['username'])
		schedules = Scheduler.objects.filter(user=user)
		serializer = SchedulerSerializer(schedules, many=True)
		return Response(serializer.data)