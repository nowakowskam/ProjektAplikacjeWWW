from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .serializer import RoomSerializer, AdditionalServiceSerializer, ReservationSerializer, OrderSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Room, AdditionalService, Order, Reservation
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, permissions, filters



class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    #
    # filterset_fields = ['room_name']
    # search_fields = ['room_name']
    # ordering_fields = ['room_name']


class AdditionalServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdditionalService.objects.all().order_by("-id")
    serializer_class = AdditionalServiceSerializer
    #filterset_fields = ['service_name']


class OrderViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all().order_by("-id")
    serializer_class = OrderSerializer


class ReservationViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all().order_by("-id")
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSets(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


