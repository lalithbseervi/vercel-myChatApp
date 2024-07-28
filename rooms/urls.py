from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('createRoom/', views.createRoom, name='createRoom'),
    path('<slug:slug>/', views.room, name='room'),
]