from django.urls import path
from contents.views import ContentList, AddContent

urlpatterns = [
	path('', ContentList.as_view()),
	path('add/', AddContent.as_view())
]
