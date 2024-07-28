import os
from django.conf import settings
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myChatApp.settings')

django_asgi_application = get_asgi_application()

import rooms.consumers_backup

async def websocket_application(scope, receive, send):
    consumer = rooms.consumers_backup.ChatConsumer(scope)

    while True:
        event = await receive()

        if event['type'] == 'websocket.connect':
            await consumer.connect()
            await send({
                'type': 'websocket.accept'
            })

        if event['type'] == 'websocket.disconnect':
            await consumer.disconnect() 
            break

        if event['type'] == 'websocket.receive':
            await consumer.receive(event)
            if event['text'] == 'ping':
                await send({
                    'type': 'websocket.send',
                    'text': 'pong!'
                })

# async def websocket_application(scope, receive, send):
#     while True:
#         event = await receive()

#         if event['type'] == 'websocket.connect':
#             await send({
#                 'type': 'websocket.accept'
#             })

#         if event['type'] == 'websocket.disconnect':
#             break

#         if event['type'] == 'websocket.receive':
#             if event['text'] == 'ping':
#                 await send({
#                     'type': 'websocket.send',
#                     'text': 'pong!'
#                 })