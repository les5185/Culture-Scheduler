from django.contrib import admin
from contents.models import Content, SpecificContent, Seat

# Register your models here.
class ContentAdmin(admin.ModelAdmin):
	model = Content
	list_display = ('title', 'genre')

class SpecificContentAdmin(admin.ModelAdmin):
	model = SpecificContent
	list_display = ('content', 'date', 'start_time', 'end_time')

class SeatAdmin(admin.ModelAdmin):
	model = Seat
	list_display = ('specific_content', 'seat_number', 'seat_type')

admin.site.register(Content, ContentAdmin)
admin.site.register(SpecificContent, SpecificContentAdmin)
admin.site.register(Seat, SeatAdmin)