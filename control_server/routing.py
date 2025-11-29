from django.urls import re_path
from control_server.consumers import ControlConsumer

websocket_urlpatterns = [
    # re_path(r'ws/control/(?P<vehicle_id>\w+)/$', consumers.ControlConsumer.as_asgi()),    # for vehicle control
    re_path(r'ws/control/$', ControlConsumer.as_asgi()),    # test route for vehicle control
]   