from django.db import models



class Reservation(models.Model):
    pass

class Room(models.Model):
    standard_list = (('podstawowy','podstawowy'),
                      ('sredni', 'sredni')
                      ('wyzszy','wyzszy'),
                     )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True)
    standard = models.CharField(max_length=20,choices=standard_list,default='podstawowy')
    reservation=models.ForeignKey(Reservation, on_delete=models.CASCADE())

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = "Pokoj"
        verbose_name_plural = "Pokoje"
