"""tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view

from core.views import PackageList, PackageState, RouteDetail, PackageEstimatedTime


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token', obtain_auth_token, name='obtain_token'),
    path('packages/', PackageList.as_view(), name='order_list'),
    path('packages/<int:pk>/state', PackageState.as_view(), name='order_state'),
    path('packages/<int:pk>/eta', PackageEstimatedTime.as_view(), name='order_eta'),
    path('routes/<int:pk>', RouteDetail.as_view(), name='route'),
    path('schema', get_schema_view(
        title="Kurztrip Tracking API",
        description="Tracking Micro Service for the Kurztrip App"
    ), name='schema_view'),
]
