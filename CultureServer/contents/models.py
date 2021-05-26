from django.db import models


class Content(models.Model):
	EXHIBITION = 'EXHIBITION'
	LECTURE = 'LECTURE'
	CONCERT = 'CONCERT'
	CULTURE_EVENT = 'CULTURE_EVENT'
	SPORTS = 'SPORTS'

	TYPE_OF_GENRE = [
		(EXHIBITION, '전시'),
		(LECTURE, '강연'),
		(CONCERT, '공연예술'),
		(CULTURE_EVENT, '문화행사'),
		(SPORTS, '스포츠'),
	]
##content 에 키워드 추가 
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

	title = models.CharField(max_length=30)
	genre = models.CharField(max_length=20, choices=TYPE_OF_GENRE)  
	cast = models.CharField(max_length=30, null=True, blank=True)
	director = models.CharField(max_length=10, null=True, blank=True)
	location = models.CharField(max_length=10)
	plot = models.CharField(max_length=200)
	image = models.ImageField(null=True, blank=True, upload_to='images')
	rate = models.IntegerField()
	preference_one = models.CharField(max_length=20, choices=TYPE_OF_PREFERENCE, null=True)
	preference_two = models.CharField( max_length=20, choices=TYPE_OF_PREFERENCE_2, null=True)
	

	def __str__(self):
		return self.title

class SpecificContent(models.Model):
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	date = models.DateField()
	total = models.IntegerField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()

	def __str__(self):
		return str(self.content) + str(self.date) + str(self.start_time)

class Seat(models.Model):
	TYPE_OF_SEAT = [
		('', 'Select'),
		('VIP', 'VIP'),
		('R', 'R'),
		('S', 'S'),
		('A', 'A'),
	]
	seat_number = models.CharField(max_length=3)
	seat_type = models.CharField(max_length=5, choices=TYPE_OF_SEAT, blank=False)
	specific_content = models.ForeignKey(SpecificContent, on_delete=models.CASCADE)
	is_reserved = models.BooleanField()

	class Meta:
		unique_together = ('seat_number', 'specific_content')

	def __str__(self):
		return self.seat_number + str(self.specific_content)
