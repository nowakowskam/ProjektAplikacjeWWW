from rest_framework import serializers
from .models import AdditionalService,Reservation, Room, Order
from django.contrib.auth.models import User
from django.db import models
from datetime import date



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['url','standard', 'price', 'room_name', 'description']

class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdditionalService
        fields=['url', 'service_name', 'description']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields=['url', 'add_service', 'client']

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Reservation
        fields=['client', 'date_from', 'date_to', 'price','room', 'url', 'total_price']
        read_only_fields=("client",)


    def validate(self, data):
        if data['date_from'] > data['date_to']:
            raise serializers.ValidationError("Finish must occur after start")
        return data



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'url']


