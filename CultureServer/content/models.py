from django.db import models

# Create your models here.
class Content(models.Model):
    rating_choice = (
      ('추천', '추천'),
      ('비추천', '비추천'),
    )
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=10)
    cast = models.CharField(max_length=30)
    director = models.CharField(max_length=10)
    runnning_time = models.IntegerField(help_text='모든 러닝 타임은 분으로 표시됩니다')
    location = models.CharField(max_length=10)
    plot = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='images')

#위에랑 아래 확인 
class Photo(models.Model):
    content_photo = models.ForeignKey('Content', on_delete=models.CASCADE, related_name='photos', verbose_name='대표 이미지')
    photo_file = models.ImageField('사진', upload_to='photo/%Y/%m/%d')
    # request.data = request.POST + request.FILES
    # request.FIELS['photo_file'] -> MEDIA_ROOT
    # path: photo.photo_file.path  MEDIA_ROOT/photo/~/~/~/~.jpg (절대 경로) - 경로에 저장
    # url: photo.photo_file.url  MEDIA_URL/photo/~/~/~/~.jpg (상대 경로) - DB에 문자열로 저장


class SpecificContent(models.Model):
    specific_information = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    #여기 어떻게 할지 고민 


