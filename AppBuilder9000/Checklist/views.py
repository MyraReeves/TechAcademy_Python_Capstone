from django.shortcuts import render, get_object_or_404, redirect
from .models import WashingtonPark


def home(request):
    parks_info = WashingtonPark.object.all()
    return render(request, 'Washington.html', {'parklist': parks_info})

