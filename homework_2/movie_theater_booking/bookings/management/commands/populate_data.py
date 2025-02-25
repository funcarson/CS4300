import random
from datetime import timedelta, date
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
from faker import Faker

#Uses faker to populate with random data
fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with random movies, seats, and bookings'

    def handle(self, *args, **kwargs):
        #Creates a user if one doesn't exist (for bookings)
        if not User.objects.filter(username='testuser').exists():
            user = User.objects.create_user(username='testuser', password='testpass')
            self.stdout.write(self.style.SUCCESS('Created testuser'))
        else:
            user = User.objects.get(username='testuser')

        #Creates random movies
        movies = []
        for _ in range(5):  # create 5 movies
            movie = Movie.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text(max_nb_chars=200),
                release_date=fake.date_between(start_date='-1y', end_date='today'),
                duration=timedelta(minutes=random.randint(80, 180))
            )
            movies.append(movie)
            self.stdout.write(self.style.SUCCESS(f'Created movie: {movie.title}'))

        #Creates random seats
        seats = []
        for row in range(1, 6):  # 5 rows
            for num in range(1, 11):  # 10 seats per row
                seat_number = f"{chr(64+row)}{num}"  # e.g., A1, A2, ..., E10
                seat = Seat.objects.create(
                    seat_number=seat_number,
                    booking_status=False
                )
                seats.append(seat)
        self.stdout.write(self.style.SUCCESS(f'Created {len(seats)} seats.'))

        #Creates 10 random bookings for seats
        booked_seats = random.sample(seats, 10)
        for seat in booked_seats:
            if not seat.booking_status:
                seat.booking_status = True
                seat.save()
                movie = random.choice(movies)
                booking = Booking.objects.create(
                    movie=movie,
                    seat=seat,
                    user=user
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Booked seat {seat.seat_number} for movie "{movie.title}"'
                ))

        self.stdout.write(self.style.SUCCESS('Database population complete.'))
