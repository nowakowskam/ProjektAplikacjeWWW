from service.models import AdditionalService
from django.test import TestCase
from service.models import Room


class AdditionalServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        AdditionalService.objects.create(
            service_name="additional service",
        )

    def test_service_name_label(self):
        additional_service = AdditionalService.objects.get(id=1)
        field_label = additional_service._meta.get_field("service_name").verbose_name
        self.assertEqual(field_label, "service name")

    def test_object_name_is_service_name(self):
        additional_service = AdditionalService.objects.get(id=1)
        expected_object_name = additional_service.service_name
        self.assertEqual(str(additional_service, expected_object_name))

    def test_description_is_blank(self):
        additional_service = AdditionalService.objects.get(id=1)
        blank = None
        self.assertEqual(additional_service.description, None)


class AdditionalServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        AdditionalService.objects.create(
            service_name="additional service",
            price="50",
        )

    def test_service_name_label(self):
        additional_service = AdditionalService.objects.get(id=1)
        field_label = additional_service._meta.get_field("service_name").verbose_name
        self.assertEqual(field_label, "service name")

    def test_object_name_is_service_name(self):
        additional_service = AdditionalService.objects.get(id=1)
        expected_object_name = additional_service.service_name
        self.assertEqual(str(additional_service.service_name), expected_object_name)

    def test_description_is_blank(self):
        additional_service = AdditionalService.objects.get(id=1)
        blank = ""
        self.assertEqual(additional_service.description, blank)
