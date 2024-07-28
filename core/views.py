from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import registerationForm
from rooms.models import Room, Message

# Create your views here.
def frontPage(request):
    user = request.user
    if user.is_authenticated:
        rooms_joined = Room.objects.filter(messages__user=user).distinct()
        context = {
            'user': user,
            'rooms_joined': rooms_joined
        }
    else:
        return render(request, 'core/frontPage.html')
        
    return render(request, 'core/frontPage.html', context)

def register(request):
    if request.method == 'POST':
        form = registerationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('frontPage')
    
    else:
        form = registerationForm()
    
    return render(request, 'core/register.html', {'form': form})

def forgotPass(request):
    return render(request, 'core/forgotPass.html')