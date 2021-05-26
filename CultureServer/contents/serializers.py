from rest_framework import serializers
from contents.models import Content, SpecificContent

class ContentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Content
		fields = [
			'pk',
			'title',
			'genre',
			'cast',
			'director',
			'location',
			'plot',
			'rate'
		]

class SpecificContentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SpecificContent
		fields = [
			'pk',
			'content',
			'date',
			'total',
			'start_time',
			'end_time',
		]
