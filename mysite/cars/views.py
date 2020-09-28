from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Car
import datetime as dt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def car_list(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'cars/cars_list.html', context)


def cross_car(request, id):
    car = get_object_or_404(Car, pk=id)
    now = dt.datetime.now()

    car.is_visited = True
    car.date = now
    car.save()
    return redirect('car_list')
