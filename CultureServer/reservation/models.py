from django.db import models

# Create your models here.

class Reservation(models.Model):
    payment_choice = (
      ('무통장 입금', '무통장 입금'),
    )
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='reservations', verbose_name='예매 내역')
    content = models.ForeignKey('Content', on_delete=models.CASCADE, related_name='contents', verbose_name='예약 상세 정보')
    timestamp = models.DateTimeField('예매 날짜')
    payment_type = models.CharField(max_length = 10, choices=payment_choice)
    paid_amount = models.IntegerField(max_length = 10)
    complete = models.BooleanField('예매 완료 여부', default=False)

    def __str__(self):
      return str(self.user) 
      # indent 어떻게 할까

class Seat(models.Model):
    seat_choice = (
      ('', 'Select'),
      ('VIP', 'VIP'),
      ('R', 'R'),
      ('S', 'S'),
      ('A', 'A'),
    )
    no = models.CharField(max_length=3)
    seat_type = models.CharField(max_length=5, choices=seat_choice, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    # 위/아래 다시 확인 그리고 show model 추가 

    class Meta:
      unique_together = ('no', 'show')
    
    def __str__(self):
      return self.no + str(self.show)

class ReservedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    class Meta:
      unique_together = ('seat', 'reservation')
    
    def __str__(self):
      return str(self.seat) + '|' + str(self.reservation)