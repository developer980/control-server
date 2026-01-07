from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
# from requests import request
import json

def authenticate_user(request, is_staff= False):
    body = request.body
    email = json.loads(body).get("email")
    password = json.loads(body).get("password")
    user = authenticate(request, username=email, password=password, is_staff=is_staff)

    if user is not None:
        print("Authenticated user:", user.id)
        return {"status": "ok",
                "message": "We sent a code to your email.", 
                "user_id": user.id, 
                "email": user.email}
    
    else:
        return {"status": "error", "message": "Invalid credentials."}

def register_user(user_data):
    username = user_data['first_name'].lower() + '_' + user_data['last_name'].lower()

    existing_username = User.objects.filter(username=username).first()
    sufix = 0
    while existing_username is not None:
        sufix += 1
        existing_username = User.objects.filter(username=username + str(sufix)).first()
    
    
    user = User.objects.create_user(
        username=username + str(sufix),
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

def fetch_user_by_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return None