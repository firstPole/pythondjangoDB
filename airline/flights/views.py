from django.shortcuts import render
import sys

from .models import Flight
# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights": Flight.objects.all()
    })
def flight(request,flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except:
        print("No such flights present!")
        sys.exit(1)
    return render(request,"flights/flight.html",{
        "flight" : flight,
        "passengers": flight.passengers.all()
    })