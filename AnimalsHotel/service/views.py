from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .serializer import RoomSerializer, AdditionalServiceSerializer, ReservationSerializer, OrderSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Room, AdditionalService, Order, Reservation
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import viewsets
from rest_framework import permissions

@api_view(["GET"])
def api_overview(request):
    api_urls = {
        "List": "/room-list/",
        "Detail View": "/room-detail/<str:pk>/",
        "Create": "/room-create/",
        "Update": "/room-update/<str:pk>/",
        "Delete": "/room-delete/<str:pk>/",
        "List": "/order-list/",
        "Detail View": "/order-detail/<str:pk>/",
        "Create": "/order-create/",
        "Update": "/order-update/<str:pk>/",
        "Delete": "/order-delete/<str:pk>/",
    }

    return Response(api_urls)


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all().order_by("-id")
    serializer_class = RoomSerializer
    filterset_fields = ['room_name']
    search_fields = ['room_name']
    ordering_fields = ['room_name']
    validators=[]

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room
    serializer_class = RoomSerializer

class AdditionalServiceList(generics.ListCreateAPIView):
    queryset = AdditionalService.objects.all().order_by("-id")
    serializer_class = AdditionalServiceSerializer
    filterset_fields = ['service_name']

class AdditonalServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdditionalService
    serializer_class = AdditionalServiceSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by("-id")
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order
    serializer_class = OrderSerializer

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all().order_by("-id")
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    #TODO Make a validation

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all().order_by("-id")
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
