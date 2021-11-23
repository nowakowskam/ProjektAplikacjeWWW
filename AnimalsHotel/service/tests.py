from django.test import TestCase
from service.models import Room

class RoomModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Room.objects.create(
            price=200,
            room_name="Test room",
            description="Sample description about "
                        "room available in AnimalsHotel.",
            standard="wyzszy",
        )

    def test_price_label_max_digits(self):
        room = Room.objects.get(id=1)
        max_digits = room._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 10)

    def test_room_name_label(self):
        room = Room.objects.get(id=1)
        field_label = room._meta.get_field('room_name').verbose_name
        self.assertEqual(field_label,'room name')

    def test_description_max_length(self):
        room = Room.objects.get(id=1)
        max_length = room._meta.get_field('description').max_length
        self.assertEqual(max_length,255)

    def test_object_name_is_room_name_coma_price(self):
        room = Room.objects.get(id=1)
        expected_object_name = f'{room.room_name}, {room.price}'
        self.assertEqual(str(room),expected_object_name)

from service.models import AdditionalService

class AdditionalServiceTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        AdditionalService.objects.create(
            service_name="additional service",
        )

    def test_service_name_label(self):
        additional_service = AdditionalService.objects.get(id=1)
        field_label = additional_service._meta.get_field('service_name').verbose_name
        self.assertEqual(field_label,'service name')

    def test_object_name_is_service_name(self):
        additional_service = AdditionalService.objects.get(id=1)
        expected_object_name = additional_service.service_name
        self.assertEqual(str(additional_service), expected_object_name)

    def test_description_is_blank(self):
        additional_service = AdditionalService.objects.get(id=1)
        blank = None
        self.assertEqual(additional_service.description, "")