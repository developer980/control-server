from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import backends, authenticate, login
# from requests import request
import json

def authenticate_user(request):
    body = request.body
    email = json.loads(body).get("email")
    password = json.loads(body).get("password")
    user = authenticate(request, username=email, password=password)

    if user is not None:
        # TODO: Add email verification if authentication succesful
        # login(request, user=user)
        print("Authenticated user:", user.id)
        return {"status": "ok",
                "message": "We sent a code to your email.", 
                "user_id": user.id, 
                "email": user.email}
    
    else:
        return {"status": "error", "message": "Invalid credentials."}

def register_user(user_data):
    username = user_data['first_name'].lower() + '_' + user_data['last_name'].lower()
    
    user = User.objects.create_user(
        username=username,
        email=user_data['email'],
        first_name=user_data.get('first_name', ''),
        last_name=user_data.get('last_name', ''),
        password=user_data['password'],
    )
    
    user.save()
    print("Registering user:", user_data)
    return HttpResponse("ok")


def fetch_users(email="", first_name="", last_name="", username=""):
    users = User.objects.all()
    
    if email:
        users = users.filter(email=email)
    if first_name:
        users = users.filter(first_name=first_name)
    if last_name:
        users = users.filter(last_name=last_name)
    if username:
        users = users.filter(username=username)
    
    return users.order_by('id')