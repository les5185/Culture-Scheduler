from django.urls import path
from contents.views import ContentList, AddContent, ContentDetail

urlpatterns = [
	path('', ContentList.as_view()),
	path('add/', AddContent.as_view()),
	path('<int:pk>/', ContentDetail.as_view())
]
