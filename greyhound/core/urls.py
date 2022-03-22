from django.urls import path

from . import views

urlpatterns = [
    path('saldo/', views.saldo),
    path('', views.index),
]