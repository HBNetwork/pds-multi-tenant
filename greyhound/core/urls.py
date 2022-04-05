from django.urls import path

from . import views

urlpatterns = [
    path('saldo/', views.saldo, name='saldo'),
    path('', views.index, name='index'),
]