from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Room, Message, User
from .forms import CreateRoomForm

# Create your views here.
@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    if room.slug == 'test':
        if request.user.is_staff or request.user.is_superuser:
            return render(request, 'room/room.html', {'room': room, 'messages': messages})
        else:
            return render(request, 'room/error.html')

    return render(request, 'room/room.html', {'room': room, 'messages': messages})

# @csrf_protect
# @login_required
# def createRoom(request):
#     if request.method == 'POST':
#         form = CreateRoomForm(request.POST or None)
#         if not form.is_valid():
#             print(request.POST)

#         if form.is_valid():
#             room_name = form.cleaned_data['room_name']
#             inp_slug = form.cleaned_data['inp_slug']

#             if Room.objects.filter(name=room_name).exists():
#                 messages.error(request, "This room name has already been used.")
#             else:
#                 new_room = form.save(commit=False)
#                 new_room = Room.objects.create(name=room_name, slug=inp_slug)
#                 new_room.save()
#                 messages.success(request, "Room created successfully!")
#                 return redirect('<slug:slug>/')
#         else:
#             messages.error(request, "Form is invalid.")
#             print(form.errors)
#     else:
#         form = CreateRoomForm()
#     return render(request, 'room/createRoom.html', {'form': form})

@login_required
def createRoom(request):
    if request.method == 'POST':
        form = CreateRoomForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            slug = form.cleaned_data['slug']
            
            if Room.objects.filter(name=name).exists():
                messages.error(request, "This room name has already been used!")
            else:
                new_room = form.save(commit=False)
                new_room = Room.objects.create(name=name, slug=slug)
                new_room.save()
                messages.success(request, "Room created successfully!")

    rooms = Room.objects.all()
    form = CreateRoomForm()
    return render(request, 'room/createRoom.html', {'form': form})