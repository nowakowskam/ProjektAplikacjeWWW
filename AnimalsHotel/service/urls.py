from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views

router = routers.SimpleRouter()


router.register(r'rooms', views.RoomList)
router.register(r'room/<int:pk>', views.RoomDetail)
router.register(r'add-service', views.AdditionalServiceList)
router.register(r'add-service/<int:pk>', views.AdditionalService)
router.register(r'orders', views.OrderList)
router.register(r'orders/<int:pk>',views.OrderDetail)
router.register(r'reservations', views.ReservationList)
router.register(r'reservations/<int:pk>', views.ReservationDetail)
router.register(r'user', views.UserList)
router.register(r'user/<int:pk>',views.UserDetail)

urlpatterns = [
    path('', include(router.urls)),
]
