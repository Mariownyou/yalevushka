from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show', views.car_list, name='car_list'),
    path('saw/<int:id>', views.cross_car, name='saw')
]