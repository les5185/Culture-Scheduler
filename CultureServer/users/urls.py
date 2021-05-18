from django.urls import path
from users.views import current_user, UserList

urlpatterns = [
	path('current_user/', current_user),
	path('users/', UserList.as_view()),
]
