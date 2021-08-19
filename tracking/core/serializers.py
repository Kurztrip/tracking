from rest_framework import serializers

from .models import Package, Route, DriverRouteLink


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id', 'truck_id', 'state', 'estimated_time'
        ]


class PackageIdStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id', 'state'
        ]


class PackageStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'state'
        ]


class PackageIdETASerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id', 'estimated_time'
        ]


class PackageETASerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'estimated_time'
        ]


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = [
            'starting_time', 'p_longitudes', 'p_latitudes'
        ]


class RouteIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = [
            'truck_id', 'starting_time', 'p_longitudes', 'p_latitudes'
        ]


class DriverRouteLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverRouteLink
        fields = [
            'driver_id', 'route_id'
        ]
