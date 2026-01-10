from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Vehicle(models.Model):
    """
    Model representing different modes of vehicle operation.
    """
    
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=50, default='utility')

    def generate_password(self, password):
        self.password = make_password(password)

    def compare_password(self, password):
        return check_password(password, self.password)

    def __str__(self):
        return self.vehicle_type