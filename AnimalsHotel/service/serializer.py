from rest_framework import serializers
from .models import Reservation, Room, Order, AdditionalService

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'