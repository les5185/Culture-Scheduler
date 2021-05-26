from django.urls import path
from contents.views import ContentList, AddContent, ContentDetail, SearchContent, CompareSchedule, getContentByPreference, getContentByGenre, CompareIndivdualSchedule

urlpatterns = [
	path('', ContentList.as_view()),
	path('add/', AddContent.as_view()),
	path('<int:pk>/', ContentDetail.as_view()),
	path('search-content/', SearchContent.as_view()),
	path('compare/', CompareSchedule.as_view()),
	path('content-by-preference/', getContentByPreference.as_view()),
	path('content-by-genre/', getContentByGenre.as_view()),
	path('compare-individual-schedule/', CompareIndivdualSchedule.as_view()),
]
