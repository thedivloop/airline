from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger
# Create your views here.

# def custom_404_view(request, exception):
#     return render(request, "404.html", status=404)

def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    try:
      flight = Flight.objects.get(pk=flight_id)
      return render(request, "flights/flight.html", {
        "flight": flight, "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights
        =flight).all()
      })
    except:
      return render(request, "404.html", status=404)

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight) 
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    return HttpResponseRedirect(reverse("index"))
