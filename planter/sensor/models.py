from django.db import models
from plant.models import Plant


class PlantSensor(models.Model):
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, null=False, related_name='sensor')
    data_type = models.CharField(max_length=200)  # todo there should be strings representing measurements and other signals

    api_key = None

    def __str__(self):
        return f"Sensor attached to {self.plant}"
