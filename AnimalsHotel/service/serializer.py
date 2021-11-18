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
    add_service=serializers.PrimaryKeyRelatedField(queryset=AdditionalService.objects.all())
    client= serializers.SerializerMethodField('_user')

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    class Meta:
        model = Order
        fields=['url', 'add_service', 'client', 'total_price']

class ReservationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    room=serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=User.get_email_field_name())

    class Meta:
        model=Reservation
        fields=['owner', 'date_from', 'date_to', 'price','room', 'user', 'url']

    def validate_date(self):
        if self.date_from > self.date_to:
            raise serializers.ValidationError("End date must be after start date.")
        if self.date_from >date.today():
            raise  serializers.ValidationError("The first date you can take is for today")



class UserSerializer(serializers.ModelSerializer):
    # order = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())
    # reservation=serializers.PrimaryKeyRelatedField(many=True, queryset=Reservation.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'url']