from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
	path('', views.api_overview, name="api-overview"),
	path('room-list/', views.room_list, name="room-list"),
	path('room-detail/<str:pk>/', views.room_detail, name="room-detail"),
	path('room-create/', views.room_create, name="room-create"),

	path('room-update/<str:pk>/', views.room_update, name="room-update"),
	path('room-delete/<str:pk>/', views.room_delete, name="room-delete"),
]
