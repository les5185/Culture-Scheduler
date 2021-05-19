from django.contrib import admin
from users.models import User, Friend

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	model = User
	list_display = ('username', 'first_name', 'last_name', 'gender')


class FriendAdmin(admin.ModelAdmin):
	model = Friend
	list_display = ('current_user',)

admin.site.register(User, UserAdmin)
admin.site.register(Friend, FriendAdmin)