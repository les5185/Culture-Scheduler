from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	gender_choices = ((
		('남성', '남성'),
		('여성', '여성'),
	))
	contact = models.CharField(verbose_name='휴대폰 번호', max_length=15)
	birth = models.DateField(verbose_name='생년월일', blank=True, null=True)
	gender = models.CharField(verbose_name='성별', max_length=5, choices=gender_choices)
	
	def __str__(self):
		return self.first_name + self.last_name