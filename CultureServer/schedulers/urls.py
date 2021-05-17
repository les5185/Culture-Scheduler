from django.urls import path
from schedulers.views import ScheduleList

urlpatterns = [
	path('', ScheduleList.as_view()),
]
