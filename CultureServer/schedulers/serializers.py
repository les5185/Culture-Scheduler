from rest_framework import serializers
from schedulers.models import Scheduler


class SchedulerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Scheduler
		fields = [
			'pk',
			'user',
			'startDate',
			'endDate',
			'title',
			'notes',
			'location'
		]
