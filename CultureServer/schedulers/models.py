from django.db import models
from users.models import User


class Scheduler(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
	startDate = models.DateTimeField()
	endDate = models.DateTimeField()
	title = models.CharField(max_length=10)
	notes = models.CharField(max_length=30, null=True)
	location = models.CharField(max_length=8)
	
	def __str__(self):
            return str(self.user) + "님의 스케줄: " + str(self.title)




