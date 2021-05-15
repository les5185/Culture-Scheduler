from django.contrib import admin
from contents.models import Content

# Register your models here.
class ContentAdmin(admin.ModelAdmin):
	model = Content

admin.site.register(Content, ContentAdmin)