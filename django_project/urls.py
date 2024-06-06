from django.urls import path
from . import views

urlpatterns = [
    path('', views.compare_devices, name='compare_devices'),
]
