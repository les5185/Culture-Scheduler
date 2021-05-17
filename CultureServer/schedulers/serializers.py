from rest_framework import serializers
from schedulers.models import Scheduler

class SchedulerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Scheduler
		fields = [
			'user',
			'date',
			'start_time',
			'end_time',
			'title',
			'info',
			'location'
		]
