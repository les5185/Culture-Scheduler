from django.urls import path
from users.views import current_user, UserList, FriendList, AddFriend, SearchUser

urlpatterns = [
	path('current_user/', current_user),
	path('users/', UserList.as_view()),
	path('friends/', FriendList.as_view()),
	path('search-user/', SearchUser.as_view()),
	path('add-friend/', AddFriend.as_view()),
]

