"""
ASGI config for control_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
from channels.security.websocket import AllowedHostsOriginValidator
from control_server.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'control_server.settings')
django.setup()

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket":
       AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    ),
})