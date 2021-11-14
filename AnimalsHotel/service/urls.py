from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", views.api_overview, name="api-overview"),
    path("api/rooms", views.RoomList.as_view()),
    path("api/rooms/<int:pk>", views.RoomDetail.as_view()),
    path("api/add-service", views.AdditionalServiceList.as_view()),
    path("api/add-service/<int:pk>", views.AdditonalServiceDetail.as_view()),
    path("api/orders", views.OrderList.as_view()),
    path("api/orders/<int:pk>", views.OrderDetail.as_view()),
    path("api/reservations", views.ReservationList.as_view()),
    path("api/reservations/<int:pk>", views.ReservationDetail.as_view()),
    path("api/user", views.UserList.as_view()),
    path("api/user/<int:pk>", views.UserDetail.as_view()),
]
