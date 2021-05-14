from django.db import models
from django.core.mail import send_mail 

# Create your models here.
'''class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('사용자의 이메일이 없습니다.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('관리자가 아닙니다.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('관리자가 아닙니다.')
        return self._create_user(email, password, **extra_fields)'''

class User(models.Model):
    gender_choices = ((
      ('남성', '남성'),
      ('여성', '여성'),
    ))
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    name = models.CharField('이름', max_length=30)
    email = models.EmailField('이메일', unique=True)
    contact = models.CharField('휴대폰 번호', max_length=15)
    birth = models.DateField('생년월일', blank=True, null=True)
    gender = models.CharField('성별', max_length=5, choices=gender_choices)

    #objects = UserManager()

    username_field = 'email'
    required_fields = []

    class Meta:
      verbose_name = ('user')
      verbose_name_plural = _('users')
    
    def __str__(self):
      return self.name 
    
    def get_name(self):
      return self.name
    
    def email_user(self, subject, message, from_email=None, **kwargs):
      send_mail(subject, message, from_email, [self.email], **kwargs)
