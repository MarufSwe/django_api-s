from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors = None

    def __str__(self):
        return self.name


class BikeHouse(models.Model):
    name = models.CharField(max_length=20)
    cc = models.IntegerField()
    model = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    place = models.OneToOneField(Place, on_delete=models.CASCADE, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors = None

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    bike_house = models.ForeignKey(BikeHouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
