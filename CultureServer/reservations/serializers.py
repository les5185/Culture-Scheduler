from rest_framework import serializers
from reservations.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = [
			'pk',
			'reserver',
			'others',
			'specific_content',
			'timestamp',
			'payment_type',
			'paid_amount',
			'is_complete'
		]
		
