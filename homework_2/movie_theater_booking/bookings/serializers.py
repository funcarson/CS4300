#Serializer
from rest_framework import serializers
from .models import Movie, Seat, Booking

#Converts Movie model instance into a JSON
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

#Converts Seat model instance into a JSON
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

#Converts Booking model instance into a JSON
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('user', 'booking_date',)

