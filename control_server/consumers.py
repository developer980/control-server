import json

from channels.generic.websocket import WebsocketConsumer


class ControlConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({"message": "Connected to Control Server"}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["command"]
        print(f"Received command: {message}")

        self.send(text_data=json.dumps({"message": message}))