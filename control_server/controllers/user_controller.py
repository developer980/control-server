from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

def authenticate_user(credentials):
    
    pass

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


    pass