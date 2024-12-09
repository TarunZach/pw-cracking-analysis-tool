# brute_force_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.brute_force_view, name='brute_force_view'),
]
