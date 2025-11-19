from django.shortcuts import render
from control_server.controllers import vehicle_controller

def home(request):
    return render(request, "home.html")

def control_vehicle(request):
    result = vehicle_controller.initiate_vehicle_control()
    return render(request, "home.html", {"result": result})