from rest_framework import serializers

from .models import Package, Route


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id', 'truck_id', 'volume', 'receiver', 'destination_long', 'destination_lat', 'sender',
            'state', 'estimated_time'
        ]


class PackageStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id', 'state'
        ]


class PackageEstimatedTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id', 'estimated_time'
        ]


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = [
            'truck_id', 'p_longitudes', 'p_latitudes', 'driver_long', 'driver_lat'
        ]
