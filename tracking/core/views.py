from rest_framework import generics
from rest_framework import mixins
import requests

from .models import Package, Route
from .serializers import PackageStateSerializer, PackageSerializer, RouteSerializer, \
    PackageIdStateSerializer, PackageETASerializer, PackageIdETASerializer, RouteIdSerializer


class PackageList(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PackageDetail(mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class = PackageStateSerializer
    queryset = Package.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PackageIdState(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    serializer_class = PackageIdStateSerializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PackageState(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    serializer_class = PackageStateSerializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PackageIdETA(mixins.RetrieveModelMixin,
                   generics.GenericAPIView):
    serializer_class = PackageIdETASerializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PackageETA(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    serializer_class = PackageETASerializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RouteList(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                generics.GenericAPIView):
    serializer_class = RouteIdSerializer
    queryset = Route.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RouteDetail(mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
