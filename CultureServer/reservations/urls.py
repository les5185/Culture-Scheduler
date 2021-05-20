from django.urls import path
from reservations.views import ReservationList, AddReservation, ReservationDetail

urlpatterns = [
	path('', ReservationList.as_view()),
	path('add-reservation/', AddReservation.as_view()),
	path('<int:pk>/', ReservationDetail.as_view()),
]
