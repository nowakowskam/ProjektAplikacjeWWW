from rest_framework import serializers
from .models import AdditionalService,Reservation, Room, Order
from django.contrib.auth.models import User
from django.db import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['pk','standard', 'price', 'room_name', 'description']

class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['pk', 'service_name', 'description']


class OrderSerializer(serializers.ModelSerializer):
    add_service=serializers.PrimaryKeyRelatedField(queryset=AdditionalService.objects.all())
    client= serializers.SerializerMethodField('_user')

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user
    class Meta:
        model = Order
        fields=['pk', 'add_service', 'client', 'total_price']

class ReservationSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField('_user')
    room=serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    class Meta:
        models=Reservation
        fields=['client', 'date_from', 'date_to', 'price','room']