from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    conversations = []
    users = User.objects.exclude(id=request.user.id)
    for user in users:
        messages = Message.objects.filter(sender=request.user, recipient=user) | Message.objects.filter(sender=user, recipient=request.user)
        
        conversation = {
            'user': user,
            'last_message': messages.last(),
            
        }
        conversations.append(conversation)
    return render(request, 'home.html', {'conversations': conversations})

@login_required
@login_required
def chat(request, user_id):
    current_user = request.user
    user = User.objects.get(id=user_id)
    messages = Message.objects.filter(sender=request.user, recipient=user) | Message.objects.filter(sender=user, recipient=request.user)
    messages = messages.order_by('timestamp')
    
    if request.method == 'POST':
        content = request.POST.get('message')
        message = Message.objects.create(sender=request.user, recipient=user, content=content)
        message.save()
    
    context = {
        'user': user,
        'messages': messages,
        'current_user' : current_user
    }
    return render(request, 'chat.html', context)

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('edit_profile')
    return render(request, 'profile.html', {'user_profile': user_profile})

