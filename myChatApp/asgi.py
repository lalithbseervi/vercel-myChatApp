import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myChatApp.settings')
django.setup()

import rooms.routing
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
     "http": get_asgi_application(),
     "websocket": AuthMiddlewareStack(
         URLRouter(
             rooms.routing.websocket_urlpatterns
         )
     )
 })

# async def application(scope, receive, send):
#     if scope['type'] == 'http':
#         await django_asgi_application(scope, receive, send)
#     elif scope['type'] == 'ws' or 'websocket':
#         await websocket_application(scope, receive, send)

# async def application(scope, receive, send):
#     if scope['type'] == 'http':
#         await get_asgi_application()(scope, receive, send)
#     elif scope['type'] == 'ws' or 'websocket':
#         await websocket_application(scope, receive, send)
