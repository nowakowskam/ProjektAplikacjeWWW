from rest_framework import serializers
from .models import AdditionalService, Reservation, Room, Order
from django.contrib.auth.models import User
from django.db import models
from datetime import date
import time


def timeConverter(date):
    """requires %Y-%m-%d"""
    return time.strptime(date, "%Y-%m-%d")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["url", "standard", "price", "room_name", "description"]

    def validate(self, data):
        if float(data["price"]) <= 50:
            raise serializers.ValidationError("Room never will be cheaper than 50!")
        return data


class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = ["url", "service_name", "description", "price"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["url", "add_service", "client"]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["client", "date_from", "date_to", "room", "url"]
        # read_only_fields=("client",)

    def validate(self, data):
        if timeConverter(str(data["date_from"])) > timeConverter(str(data["date_to"])):
            raise serializers.ValidationError("Finish must occur after start")

        if timeConverter(str(data["date_to"])) <= timeConverter(str(date.today())):
            raise serializers.ValidationError("The earliest reservation starts today")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "url"]
