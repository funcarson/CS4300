from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet, SeatViewSet, BookingViewSet,
    movie_list, seat_booking, booking_history, book_seat
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'seats', SeatViewSet, basename='seat')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    #API endpoints
    path('api/', include(router.urls)),
    #HTML endpoints:
    path('movies/', movie_list, name='movie_list'),
    path('seat-booking/', seat_booking, name='seat_booking'),
    path('booking-history/', booking_history, name='booking_history'),
    path('book_seat/<int:id>/', book_seat, name='book_seat'),
    #Home:
    path('', movie_list, name='home'),
]



