from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length = 255)
    no_of_guests = models.IntegerField()
    BookingDate = models.DateField()

class Menu(models.Model):
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits = 10, decimal_places = 2)
    Inventory = models.IntegerField()

