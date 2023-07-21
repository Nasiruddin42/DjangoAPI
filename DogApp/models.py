from django.db import models

# Create your models here.
class DogShop(models.Model) :
    name = models.CharField(max_length=50)
    price = models.FloatField()
    breed = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name