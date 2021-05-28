from rest_framework import serializers
from contents.models import Content, SpecificContent

class ContentSerializer(serializers.HyperlinkedModelSerializer):
	image = serializers.ImageField(use_url=True)
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
			'rate',
			'image'
		]

class SpecificContentsSerializer(serializers.ModelSerializer):
	content = ContentSerializer()
	
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
