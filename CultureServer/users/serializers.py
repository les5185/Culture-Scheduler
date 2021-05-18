from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from users.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'birth', 'contact', 'preference')

class UserSerializerWithToken(serializers.ModelSerializer):
	token = serializers.SerializerMethodField()
	password = serializers.CharField(write_only=True)

	def get_token(self, obj):
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_enconde_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(obj)
		token = jwt_enconde_handler(payload)

		return token

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save() ## save into database
		return instance

	class Meta:
		model = User
		fields = ('token', 'username', 'password', 'first_name', 'last_name', 'email', 'gender', 'birth', 'contact', 'preference')