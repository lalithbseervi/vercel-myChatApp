import os
from django.conf import settings
from django.core.asgi import get_asgi_application
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Message

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myChatApp.settings')

django_asgi_application = get_asgi_application()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming message
        pass

async def websocket_application(scope, receive, send):
    # Check if the path starts with '/ws/'
    if scope['path'].startswith('/ws/'):
        # Extract the room name from the path
        room_name = scope['path'][4:].strip('/')
        
        # Initialize the ChatConsumer with the provided room name
        consumer = ChatConsumer()

        # Route the WebSocket connection to the appropriate consumer
        await consumer(scope, receive, send)
    else:
        # Route other types of connections to the Django ASGI application
        await django_asgi_application(scope, receive, send)
