import email
from control_server.controllers import user_controller, vehicle_controller, session_controller
from django.contrib.auth.models import User, Group
from django.contrib.auth import backends, authenticate, login
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, cookie, HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import render
import json
import jwt

def admin_authenticate(request):
    body = json.loads(request.body)
    user_login_response = user_controller.authenticate_user(request, is_staff=True)

    if user_login_response["status"] != "ok":
        return JsonResponse(user_login_response)

    user = user_controller.fetch_user_by_id(user_login_response["user_id"])
    login(request, user=user)
    response = HttpResponse(JsonResponse({**user_login_response, "redirect_url": "/c-admin/dashboard/"}), content_type="application/json")

    return response

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def admin_login(request):
    print("request", request)
    return render(request, "admin_login.html")


def control_vehicle(request):
    vehicle_controller.initiate_vehicle_control()
    return render(request, "control.html", {"result": "ok"})


def home(request):
    user_id = dict(request.session.items()).get('_auth_user_id')

    user = User.objects.get(id=user_id) if user_id else None
    if user is None:
        return HttpResponseRedirect('/auth/login/')
    user_data = {"id": user.id, "username": user.username, "email": user.email, "first_name": user.first_name, "last_name": user.last_name} if user else None
    print("user", user_data)
    print("authenticated", request.user.is_authenticated)
    return render(request, "home.html", {"user": user_data})

def login_portal(request):
    if request.method != "GET":
        return render(request, "login.html", {"error": "Invalid request method."})

    print("request", request)
    return render(request, "login.html")

def login_view(request):
    user_login_response = user_controller.authenticate_user(request)

    if user_login_response["status"] != "ok":
        return JsonResponse(user_login_response)

    token = session_controller.genetate_otp_code(user_login_response["user_id"], user_login_response["email"])
    response = HttpResponse(JsonResponse({**user_login_response, "redirect_url": "/redirect/otp/"}), content_type="application/json")
    response.set_cookie("verification_token", token, httponly=True)

    print("user_login_response", user_login_response["email"])


    print("sending resaponse", response)
    return response

def otp_verify_view(request):
    return render(request, "otp_verification.html")

def otp_verify(request):
    if request.method != "POST":
        return JsonResponse({"status": "error", "message": "Invalid request method."})  
    
    token_validation_result = session_controller.otp_verify(request)
    if token_validation_result["status"] != "ok":
        return JsonResponse(token_validation_result)
    
    print("token_validation_result", token_validation_result)
    
    redirect_url = "/"

    user = User.objects.get(id=token_validation_result.get("decoded_token").get("id"))

    if(user.is_staff is True):
        redirect_url = "/c-admin/dashboard/"
    print("user", user)
    login(request, user=user)

    # TODO: add cookie deletion for verification_token
    return JsonResponse({"status": "ok", "message": "OTP verified successfully.", "redirect_url": redirect_url})

def register(request):
    if request.method != "POST":
        return JsonResponse({"status": "error", "message": "Invalid request method."})  
    
    user_data = json.loads(request.body)
    
    user_controller.register_user(user_data)
    print("Registered user:", user_data)
    return JsonResponse({"status": "ok", "message": "Registration successful."})

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
