from rest_framework import serializers
from schedulers.models import Scheduler


class SchedulerSerializer(serializers.ModelSerializer):


	class Meta:
		model = Scheduler
		fields = [
			'pk',
			'user',
			'date',
			'start_time',
			'end_time',
			'title',
			'info',
			'location'
		]
