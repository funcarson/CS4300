from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import timedelta, date
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

#Tests for Movie Model
class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A movie for testing.",
            release_date=date(2025, 1, 1),
            duration=timedelta(hours=1, minutes=30)  
        )

    def test_movie_str(self):
        #Ensures that __str__ returns the title
        self.assertEqual(str(self.movie), "Test Movie")

#Test for Seat Model
class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(
            seat_number="A1",
            booking_status=False
        )

    def test_seat_str(self):
        #Ensures __str__ returns the seat number 
        self.assertEqual(str(self.seat), "A1")

#Booking Model Test
class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A movie for testing.",
            release_date=date(2025, 1, 1),
            duration=timedelta(hours=1, minutes=30)
        )
        self.seat = Seat.objects.create(seat_number="A1", booking_status=False)
        self.booking = Booking.objects.create(
            user=self.user,
            movie=self.movie,
            seat=self.seat
        )

    def test_booking_str(self):
        #Checks that the __str__ output includes booking info
        self.assertIn(self.user.username, str(self.booking))
        self.assertIn(self.movie.title, str(self.booking))

#Movie API Test
class MovieAPITest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A movie for testing.",
            release_date=date(2025, 1, 1),
            duration=timedelta(hours=1, minutes=30)
        )
        #The DefaultRouter creates route names like 'movie-list'
        self.url = reverse('movie-list')

    def test_list_movies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #Expects a list response
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

#Seat API Test
class SeatAPITest(APITestCase):
    def setUp(self):
        self.seat = Seat.objects.create(
            seat_number="A1",
            booking_status=False
        )
        self.url = reverse('seat-list')

    def test_list_seats(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

#Booking API test
class BookingAPITest(APITestCase):
    def setUp(self):
        #Creates and logs in a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A movie for testing.",
            release_date=date(2025, 1, 1),
            duration=timedelta(hours=1, minutes=30)
        )
        self.seat = Seat.objects.create(
            seat_number="A1",
            booking_status=False
        )
        self.url = reverse('booking-list')

    def test_create_booking(self):
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #Checks if the booking appears in the list
        get_response = self.client.get(self.url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(get_response.data), 1)