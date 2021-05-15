from django.db import models
from contents.models import SpecificContent
from users.models import User
# Create your models here.


class Reservation(models.Model):
	payment_choice = [
		('무통장 입금', '무통장 입금'),
	]

	reserver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', verbose_name='예약자')
	compainion = models.ManyToManyField(User, blank=True)
	others = models.IntegerField(null=True, blank=True)
	specific_content = models.ForeignKey(SpecificContent, on_delete=models.CASCADE, related_name='specific_content', verbose_name='예매 컨텐츠 정보')
	timestamp = models.DateTimeField(auto_now_add=True)
	payment_type = models.CharField(max_length=10, choices=payment_choice)
	paid_amount = models.IntegerField()
	is_complete = models.BooleanField(verbose_name='예매 완료 여부', default=False)

	def __str__(self):
		return str(self.reserver)
		# indent 어떻게 할까
