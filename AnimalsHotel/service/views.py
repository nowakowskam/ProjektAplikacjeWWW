from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .serializer import RoomSerializer, AdditionalServiceSerializer, ReservationSerializer, OrderSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Room, AdditionalService, Order, Reservation
#from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import viewsets
from rest_framework import permissions


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # filterset_fields = ['room_name']
    # search_fields = ['room_name']
    # ordering_fields = ['room_name']


class AdditionalServiceViewSet(viewsets.ModelViewSet):
    queryset = AdditionalService.objects.all().order_by("-id")
    serializer_class = AdditionalServiceSerializer
    #filterset_fields = ['service_name']


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-id")
    serializer_class = OrderSerializer


class ReservationViewSets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by("-id")
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    #TODO Make a validation



class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


