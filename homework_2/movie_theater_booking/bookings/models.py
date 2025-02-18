from django.db import models
from django.contrib.auth.models import User

#Create the 3 models (Movie, Seat, and Bookings)

#Movie Model
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.DurationField()

def __str__(self):
    return self.title

#Seat Model
class Seat(models.Model):
    seat_number = models.CharField(max_length=5)
    booking_status = models.BooleanField(default= False)

def __str__(self):
    return self.seat_number

#Booking Model
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"
