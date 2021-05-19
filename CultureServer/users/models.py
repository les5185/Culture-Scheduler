from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	TYPE_OF_GENDER = (
		('남성', '남성'),
		('여성', '여성'),
	)

	TYPE_OF_PREFERENCE = (
		('뮤지컬', '뮤지컬'),
		('연극', '연극'),
		('전시회', '전시회'),
		('강연', '강연'),
	)

	contact = models.CharField(verbose_name='휴대폰 번호', max_length=15)
	birth = models.DateField(verbose_name='생년월일', blank=True, null=True)
	gender = models.CharField(verbose_name='성별', max_length=5, choices=TYPE_OF_GENDER)
	preference = models.CharField(verbose_name='취향', max_length=5, choices=TYPE_OF_PREFERENCE)
	
	def __str__(self):
		return self.username


class Friend(models.Model):
	users = models.ManyToManyField(User, default='users', blank=True, related_name='users')
	current_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, null=True)

	@classmethod
	def make_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(current_user=current_user)
		friend.users.add(new_friend)
	@classmethod
	def lose_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(current_user=current_user)
		friend.users.remove(new_friend)