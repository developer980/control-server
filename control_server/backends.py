from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class LoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, is_staff=False):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username, is_staff=is_staff)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None