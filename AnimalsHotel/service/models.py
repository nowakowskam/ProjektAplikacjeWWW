from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta


class Room(models.Model):
    """Room model."""

    standard_list = (
        ("podstawowy", "podstawowy"),
        ("sredni", "sredni"),
        ("wyzszy", "wyzszy"),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True)
    standard = models.CharField(
        choices=standard_list, max_length=20, default="podstawowy"
    )

    class Meta:
        verbose_name = "Pokoj"
        verbose_name_plural = "Pokoje"

    def __str__(self):
        return f"{self.room_name}, {self.price}"


class Reservation(models.Model):
    """Reservation model."""

    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)

    # def calculate_price_for_days(self, start, end):
    #     start=self.date_from
    #     end=self.date_to
    #     return (start - end) * room.price()

    class Meta:
        verbose_name = "Rezerwacja"
        verbose_name_plural = "Rezerwacje"


class AdditionalService(models.Model):
    """AdditionalService model model."""

    description = models.CharField(max_length=255, blank=True)
    service_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Dodatkowa usluga"
        verbose_name_plural = "Dodatkowe uslugi"

    def __str__(self):
        return self.service_name


class Order(models.Model):
    """Order model."""

    add_service = models.ForeignKey(AdditionalService, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Zamowienie"
        verbose_name_plural = "Zamowienia"
