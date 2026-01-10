"""
URL configuration for controlserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/login/', views.login_view, name='authenticate'),
    path('api/auth/otp-check/', views.otp_verify, name='otp_verify'),
    path('api/c-admin/auth/login/', views.admin_authenticate, name='admin_authenticate'),
    path('api/c-admin/auth/register/', views.register, name='register'),
    path("api/c-admin/add_vehicle/", views.add_vehicle, name="add_vehicle"),
    path("api/c-admin/vehicles/login/", views.vehicle_login_view, name="vehicle_login"),
    path("api/c-admin/vehicles/update/", views.update_vehicle_view, name="add_vehicle"),
    path('auth/login/', views.login_portal, name='login'),
    path('c-admin/auth/login/', views.admin_login, name='admin_login'),
    path('c-admin/dashboard/', views.UsersView.as_view(), name='admin_dashboard'),
    path('c-admin/users/', views.UsersView.as_view(), name='users'),
    path('c-admin/add-user/', views.add_user_view, name='add_user'),
    path('c-admin/vehicles/', views.VehiclesView.as_view(), name='vehicles'),
    path('c-admin/add_vehicle/', views.add_vehicle_view, name='add_vehicle'),
    path('control/', views.control_vehicle, name='control'),
    path('redirect/otp/', views.otp_verify_view, name='otp_redirect'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
