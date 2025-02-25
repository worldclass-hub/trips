from django.shortcuts import render
from .models import Destination

def home(request):
    destinations = Destination.objects.all()
    return render(request, "trips/home.html", {"destinations": destinations})


def find_guide(request):
    return render(request, 'trips/find_guide.html')