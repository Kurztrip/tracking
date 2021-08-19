from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class Route(models.Model):
    truck_id = models.IntegerField(primary_key=True)
    starting_time = models.DateTimeField(null=True)
    p_longitudes = ArrayField(models.FloatField(), blank=True, null=True)
    p_latitudes = ArrayField(models.FloatField(), blank=True, null=True)

    def __str__(self):
        return str(self.truck_id)


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    truck_id = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='package_truck', null=True, blank=True)
    state = models.CharField(max_length=15)
    estimated_time = models.DateTimeField(null=True)

    def __str__(self):
        return str(str(self.id) + ' ' + self.state)


class DriverRouteLink(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    route_id = models.OneToOneField(Route, on_delete=models.CASCADE, related_name='link_route')

    def __str__(self):
        return str(str(self.id) + ' ' + str(self.route_id))
