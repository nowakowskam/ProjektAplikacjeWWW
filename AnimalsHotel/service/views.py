from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import RoomSerializer
from .models import Room


@api_view(["GET"])
def api_overview(request):
    api_urls = {
        "List": "/room-list/",
        "Detail View": "/room-detail/<str:pk>/",
        "Create": "/room-create/",
        "Update": "/room-update/<str:pk>/",
        "Delete": "/room-delete/<str:pk>/",
    }

    return Response(api_urls)


@api_view(["GET"])
def room_list(request):
    rooms = Room.objects.all().order_by("-id")
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def room_detail(request, pk):
    rooms = Room.objects.get(id=pk)
    serializer = RoomSerializer(rooms, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def room_create(request):
    serializer = RoomSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def room_update(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(instance=room, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def room_delete(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()

    return Response("Item succsesfully delete!")
