"""honeyrae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from repairsapi.views import CustomerView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import register_user, login_user
from repairsapi.views import ServiceTicketView
from repairsapi.views import EmployeeView

router = routers.DefaultRouter(trailing_slash=False) #
router.register(r'customers', CustomerView, 'customer')

router_1 = routers.DefaultRouter(trailing_slash=False) #
router_1.register(r'employees', EmployeeView, 'employee')

router_2 = routers.DefaultRouter(trailing_slash=False) #
router_2.register(r'service_tickets', ServiceTicketView, 'serviceTicket')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(router_1.urls)),
    path('', include(router_2.urls)),
]
