from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


router.register(r'rooms', views.RoomViewSet)
router.register(r'add-service', views.AdditionalServiceViewSet)
router.register(r'orders', views.OrderViewSets)
router.register(r'reservations', views.ReservationViewSets)
router.register(r'user', views.UserViewSets)
urlpatterns = [
    path('', include(router.urls)),
]
