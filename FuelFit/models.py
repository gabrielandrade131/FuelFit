from django.db import models

# Create your models here.


class Car(models.Model):
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    gasoline_consumption = models.IntegerField()
    ethanol_consumption = models.IntegerField()

    def __str__(self):
        return f"{self.model} {self.year}"


class Price(models.Model):
    gasoline_price = models.DecimalField(max_digits=6, decimal_places=3)
    ethanol_price = models.DecimalField(max_digits=6, decimal_places=3)
