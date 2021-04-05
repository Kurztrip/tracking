from rest_framework import generics
from rest_framework import mixins
import requests

from .models import Package, Route
from .serializers import PackageStateSerializer, PackageSerializer, PackageEstimatedTimeSerializer, RouteSerializer

class PackageList(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  generics.GenericAPIView):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PackageState(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    serializer_class = PackageStateSerializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PackageEstimatedTime(mixins.RetrieveModelMixin,
                           generics.GenericAPIView):
    serializer_class = PackageEstimatedTimeSerializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RouteDetail(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
