from django.db import models

class Vehicle(models.Model):
    """
    Model representing different modes of vehicle operation.
    """
    
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255)
    vehicle_id = models.IntegerField(unique=True)
    vehicle_type = models.CharField(max_length=50, default='utility')

    def __str__(self):
        return self.name