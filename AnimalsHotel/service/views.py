from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import RoomSerializer
from .models import Room
@api_view(['GET'])
def api_overwiew(request):
    api_urls = {
        'List':'/room/list/',
        'Detail View': '/room-details/<str:pk>/',
        'Create': '/room-create/',
        'Update': '/room-update/<str:pk>/',
        'Delete': '/room-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def room_list(request):
    rooms = Room.object.all()
    serializer =RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def room_list(request, pk):
    rooms = Room.object.all()
    serializer =RoomSerializer(rooms, many=True)
    return Response(serializer.data)







# def about(request):
#     return HttpResponse('about')
#
# def home(request):
#     return  HttpResponse('home')