from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    """Reservation model."""

    client= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_from=models.DateField()
    date_to=models.DateField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Rezerwacja"
        verbose_name_plural = "Rezerwacje"


class Room(models.Model):
    """Room model."""

    # standard_list = [('podstawowy','podstawowy'),
    #                   ('sredni', 'sredni')
    #                   ('wyzszy','wyzszy')
    #                  ]
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True)
    standard = models.CharField(max_length=20,default='podstawowy') #choices=standard_list,
    reservation=models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = "Pokoj"
        verbose_name_plural = "Pokoje"

class AdditionalService(models.Model):
    """AccountsUser model model."""

    description = models.CharField(max_length=255, blank=True)
    service_name = models.CharField(max_length=20)

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = "Dodatkowa usluga"
        verbose_name_plural = "Dodatkowe uslugi"


class Order(models.Model):
    """Order model."""

    add_service=models.ForeignKey(AdditionalService, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2, null=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Zamowienie"
        verbose_name_plural = "Zamowienia"
