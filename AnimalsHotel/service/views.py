from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .serializer import RoomSerializer, AdditionalServiceSerializer, ReservationSerializer, OrderSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Room, AdditionalService, Order, Reservation
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, permissions, filters
from rest_framework.filters import SearchFilter, OrderingFilter



class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields=['id', 'room_name', 'standard']


class AdditionalServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdditionalService.objects.all().order_by("-id")
    serializer_class = AdditionalServiceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['service_name']


class OrderViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all().order_by("-id")
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['client']

class ReservationViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all().order_by("-id")
    serializer_class = ReservationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    total_price_object=Reservation()
    #total_price_object.calculate_price_for_days(Reservation.date_to, Reservation.date_from)
    search_fields = ['client', 'date_from', 'date_to']

class UserViewSets(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id']


