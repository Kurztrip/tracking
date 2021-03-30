from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializers import OrderSerializer
from .models import Order


class OrderList(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class OrderList(APIView):
#
#     permission_classes = (IsAuthenticated, )
#
#     def get(self, request, *args, **kwargs):
#         qs = Order.objects.all()
#         serializer = OrderSerializer(qs, many=True)
#         return Response(serializer.data)  # safe = False
#
#     def post(self, request, *args, **kwargs):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data, status=400)
