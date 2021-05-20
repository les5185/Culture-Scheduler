from rest_framework import serializers
from reservations.models import Reservation
from users.serializers import UserSerializer
from users.models import User

class ReservationSerializer(serializers.ModelSerializer):
	companion = UserSerializer(read_only=True, many=True)
	class Meta:
		model = Reservation
		fields = [
			'pk',
			'reserver',
			'companion',
			'others',
			'specific_content',
			'timestamp',
			'payment_type',
			'paid_amount',
			'is_complete'
		]
