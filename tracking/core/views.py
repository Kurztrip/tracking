from rest_framework import generics
from rest_framework import mixins
from rest_framework import views
from rest_framework import response

from .models import Package, Route, DriverRouteLink
from .serializers import PackageStateSerializer, PackageSerializer, RouteSerializer, \
    PackageIdStateSerializer, PackageETASerializer, PackageIdETASerializer, RouteIdSerializer, \
    DriverRouteLinkSerializer
from django_filters.rest_framework import DjangoFilterBackend


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


class DriverRouteLinkDetail(mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    serializer_class = DriverRouteLinkSerializer
    queryset = DriverRouteLink.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DriverRouteLinkList(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          generics.GenericAPIView):
    serializer_class = DriverRouteLinkSerializer
    queryset = DriverRouteLink.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['driver_id', 'route_id']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NotAssignedRoutes(views.APIView):
    serializer_class = RouteSerializer

    def get(self, request):
        assigned_routes = [route.route_id for route in DriverRouteLink.objects.all()]
        print(assigned_routes)
        trucks = [route.truck_id for route in Route.objects.all() if
                  route not in assigned_routes]
        return response.Response(trucks)
