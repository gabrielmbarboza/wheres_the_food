"""wtf URL Configuration

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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from kitchens.api.viewsets import KitchenViewSet
from addresses.api.viewsets import AddressViewSet
from meals.api.viewsets import MealViewSet
from customers.api.viewsets import CustomerViewSet
from orders.api.viewsets import OrderViewSet

router = routers.DefaultRouter()
router.register(r'kitchens', KitchenViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'meals', MealViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
