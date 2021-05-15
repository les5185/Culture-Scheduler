from django.contrib import admin
from reservations.models import Reservation

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
	model = Reservation
	list_display = ('specific_content', 'timestamp')

admin.site.register(Reservation, ReservationAdmin)