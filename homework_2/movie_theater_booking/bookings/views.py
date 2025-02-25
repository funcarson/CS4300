from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

#ViewSets for the API
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        #Limits booking history to only the logged in user
        user = self.request.user
        if user.is_authenticated:
            return Booking.objects.filter(user=user)
        return Booking.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#HTML Views for rendering templates

#Renders a page showing available movies.
def movie_list(request):
    print("movie_list view called")
    movies = Movie.objects.all()
    return render(request, 'booking/movie_list.html', {'movies': movies})

#Renders a seat booking page. Optionally filters seats by movie if a movie is selected.
def seat_booking(request):
    print("seat_booking view called")
    movies = Movie.objects.all()
    seats = None
    if 'movie_id' in request.GET:
        seats = Seat.objects.filter(booking_status=False)
    return render(request, 'booking/seat_booking.html', {'movies': movies, 'seats': seats})
#Renders a page showing the booking history for the logged in user.
def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_history.html', {'bookings': bookings})
#A simple view to book a seat.
def book_seat(request, id):
    seat = get_object_or_404(Seat, id=id)
    if not seat.booking_status:
        seat.booking_status = True
        seat.save()
        movie = Movie.objects.first()
        #Creates the booking.
        Booking.objects.create(movie=movie, seat=seat, user=None)
    return redirect('booking_history')
