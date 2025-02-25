from django.shortcuts import render
from .models import Destination

def home(request):
    destinations = Destination.objects.all()
    return render(request, "trips/home.html", {"destinations": destinations})


def find_guide(request):
    return render(request, 'trips/find_guide.html')


def dashboard(request):
    return render(request, 'trips/dashboard.html')


def add_to_cart(request):
    return render(request, 'trips/add_to_cart.html')


def payment_method(request):
    return render(request, 'trips/payment_method.html')


def success_page(request):
    return render(request, 'trips/success_page.html')


def coming_soon(request):
    return render(request, 'trips/coming_soon.html')


def about_us(request):
    return render(request, 'trips/about_us.html')


def pricing(request):
    return render(request, 'trips/pricing.html')


def services(request):
    return render(request, 'trips/services.html')


def view_more(request):
    return render(request, 'trips/view_more.html')
