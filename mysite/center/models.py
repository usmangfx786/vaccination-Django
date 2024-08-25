from django.db import models
from vaccine.models import Vaccine
# Create your models here.
class Center(models.Model):
    name = models.CharField("Center_name", max_length=32)
    adress = models.TextField("Address", max_length=500)

    def __str__(self):
        return self.name


class Storage(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    total_quantity = models.IntegerField(default=0)
    booked_quantity = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.center.name} | {self.vaccine.name}"

