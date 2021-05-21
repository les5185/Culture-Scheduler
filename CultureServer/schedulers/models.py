from django.db import models
from users.models import User


class Scheduler(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
	date = models.DateField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	title = models.CharField(max_length=10)
	info = models.CharField(max_length=20)
	location = models.CharField(max_length=8)
	
	def __str__(self):
		return str(self.user) + "님의 스케줄: " + str(self.date)




