from django.contrib import admin
from users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	model = User
	list_display = ('username', 'first_name', 'last_name', 'gender')

admin.site.register(User, UserAdmin)