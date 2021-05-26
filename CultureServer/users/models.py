from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	EXHIBITION = 'EXHIBITION'
	LECTURE = 'LECTURE'
	CONCERT = 'CONCERT'
	CULTURE_EVENT = 'CULTURE_EVENT'
	SPORTS = 'SPORTS'
	
	TYPE_OF_GENDER = (
		('남성', '남성'),
		('여성', '여성'),
	)
	TYPE_OF_GENRE = (
		(EXHIBITION, '전시'),
		(LECTURE, '강연'),
		(CONCERT, '공연예술'),
		(CULTURE_EVENT, '문화행사'),
		(SPORTS, '스포츠'),
	)
	
	TYPE_OF_PREFERENCE = (
		('유쾌한', '유쾌한'),
		('감동적인', '감동적인'),
		('스릴있는', '스릴있는'),
		('어두운', '어두운'),
		('힐링', '힐링'),
		('설레는', '설레는'),
		('잔잔한', '잔잔한'),
		('역동적인', '역동적인'),
		('유익한', '유익한'),
		('사진 찍기 좋은', '사진 찍기 좋은'),
		('장르물', '장르물'),
		('온택트', '온택트'),
	)

	TYPE_OF_PREFERENCE_2 = (
		('유쾌한', '유쾌한'),
		('감동적인', '감동적인'),
		('스릴있는', '스릴있는'),
		('어두운', '어두운'),
		('힐링', '힐링'),
		('설레는', '설레는'),
		('잔잔한', '잔잔한'),
		('역동적인', '역동적인'),
		('유익한', '유익한'),
		('사진 찍기 좋은', '사진 찍기 좋은'),
		('장르물', '장르물'),
		('온택트', '온택트'),
	)

	contact = models.CharField(verbose_name='휴대폰 번호', max_length=15)
	birth = models.DateField(verbose_name='생년월일', blank=True, null=True)
	gender = models.CharField(verbose_name='성별', max_length=5, choices=TYPE_OF_GENDER)
	genre = models.CharField(max_length=20, choices=TYPE_OF_GENRE, null=True) 
	preference_one = models.CharField(verbose_name='취향1', max_length=20, choices=TYPE_OF_PREFERENCE)
	preference_two = models.CharField(verbose_name='취향2', max_length=20, choices=TYPE_OF_PREFERENCE_2)
	
	
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