from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Route(models.Model):
    truck_id = models.IntegerField(primary_key=True)
    p_longitudes = ArrayField(models.FloatField(), blank=True, null=True)
    p_latitudes = ArrayField(models.FloatField(), blank=True, null=True)
    driver_long = models.FloatField(null=True)
    driver_lat = models.FloatField(null=True)

    def __str__(self):
        return str(self.truck_id)


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    truck_id = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='package_truck', null=True, blank=True)
    volume = models.FloatField()
    receiver = models.CharField(max_length=15)
    destination_long = models.FloatField()
    destination_lat = models.FloatField()
    sender = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    estimated_time = models.DateTimeField(null=True)

    def __str__(self):
        return str(str(self.id) + ' ' + self.state)