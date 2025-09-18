from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length = 100)
    brand = models.CharField(max_length = 100)
    price = models.IntegerField()
    color = models.CharField(max_length= 50)

    def __str__(self):
        return f"{self.brand} {self.name}"
    
