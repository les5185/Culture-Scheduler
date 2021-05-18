from django.urls import path
from schedulers.views import ScheduleList, AddSchedule, ScheduleDetail

urlpatterns = [
	path('', ScheduleList.as_view()),
	path('add/', AddSchedule.as_view()),
	path('<int:pk>/', ScheduleDetail.as_view()),

]
