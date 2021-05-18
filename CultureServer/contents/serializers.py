from rest_framework import serializers
from contents.models import Content

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