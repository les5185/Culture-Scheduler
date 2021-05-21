from django.urls import path
from contents.views import ContentList, AddContent, ContentDetail, SearchContent

urlpatterns = [
	path('', ContentList.as_view()),
	path('add/', AddContent.as_view()),
	path('<int:pk>/', ContentDetail.as_view()),
	path('search-content/', SearchContent.as_view())
]
