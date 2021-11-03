from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns=[
             path('room-list',views.room_list, name='room-list'),
             ]