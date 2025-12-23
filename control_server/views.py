import email
from control_server.controllers import user_controller, vehicle_controller 
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.shortcuts import render
import json


def admin_authenticate(request):
    # Implement authentication logic here
    user_data = json.loads(request.body)
    print(body)
    return JsonResponse({"status": "ok", "message": "We sent a code to your email."})

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def admin_login(request):
    print("request", request)
    return render(request, "admin_login.html")

def authenticate(request, email, password):
    # Implement authentication logic here
    print(email, password)
    return render(request, "login.html")
    pass

def control_vehicle(request):
    vehicle_controller.initiate_vehicle_control()
    return render(request, "control.html", {"result": "ok"})

class UsersView(ListView):
    context_object_name = "users"
    template_name = "admin_dashboard.html"
    paginate_by = 10

    def get_queryset(self):
        email = self.request.GET.get('email')
        first_name = self.request.GET.get('first_name')
        last_name = self.request.GET.get('last_name')
        username = self.request.GET.get('username')

        return user_controller.fetch_users(email, first_name, last_name, username).values("id", "username", "email", "first_name", "last_name")
        
    
    

def home(request):
    return render(request, "home.html")

def login(request):
    # response = "Please enter the code sent to your email."
    if request.method != "GET":
        return render(request, "login.html", {"error": "Invalid request method."})

    print("request", request)
    # return {"status": "ok", "message": response}
    return render(request, "login.html")

def register(request):
    if request.method != "POST":
        # Handle registration logic here
        return JsonResponse({"status": "error", "message": "Invalid request method."})  
    
    user_data = json.loads(request.body)
    
    user_controller.register_user(user_data)
    print("Registered user:", user_data)
    return JsonResponse({"status": "ok", "message": "Registration successful."})
