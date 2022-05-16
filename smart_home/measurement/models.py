from django.db import models
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

class Measurement(models.Model):
    id = models.IntegerField()
    name = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateTimeField()