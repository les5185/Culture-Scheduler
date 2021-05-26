from django.contrib import admin
from schedulers.models import Scheduler

# Register your models here.
class SchedulerAdmin(admin.ModelAdmin):
	model = Scheduler
	list_display = ('user', 'title', 'startDate', 'endDate')


admin.site.register(Scheduler, SchedulerAdmin)