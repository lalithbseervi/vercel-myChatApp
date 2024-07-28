# from django.urls import path
# from . import consumers_backup

# websocket_urlpatterns = [
#     path('ws/<str:room_name>/', consumers_backup.ChatConsumer.as_asgi()),
# ]
from django.urls import path
from . import consumers_backup, consumers

websocket_urlpatterns = [
    path('myChatApp/rooms/<str:room_name>/', consumers_backup.ChatConsumer.as_asgi()),
]