from django.db import models


class Content(models.Model):
	EXHIBITION = 'EXHIBITION'
	LECTURE = 'LECTURE'
	CONCERT = 'CONCERT'
	CULTURE_EVENT = 'CULTURE_EVENT'
	SPORTS = 'SPORTS'

	TYPE_OF_GENRE = [
		(EXHIBITION, '전시회'),
		(LECTURE, '강연'),
		(CONCERT, '영화'),
		(CULTURE_EVENT, '문화행사'),
		(SPORTS, '스포츠'),
	]

	title = models.CharField(max_length=30)
	genre = models.CharField(max_length=10, choices=TYPE_OF_GENRE)  # 초이스로 바꾸기
	cast = models.CharField(max_length=30, null=True, blank=True)
	director = models.CharField(max_length=10, null=True, blank=True)
	location = models.CharField(max_length=10)
	plot = models.CharField(max_length=200)
	image = models.ImageField(null=True, blank=True, upload_to='images')
	rate = models.IntegerField()

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
