from django.urls import path
from reservations.views import ReservationList, AddReservation, ReservationDetail

urlpatterns = [
	path('reservation_list/', ReservationList.as_view()),
	path('add_reservation/', AddReservation.as_view()),
	path('reservation_detail/', ReservationDetail.as_view()),
]
