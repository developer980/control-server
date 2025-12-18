from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse

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