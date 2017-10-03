# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,User
from django.shortcuts import render, redirect
from .models import Message 
from datetime import datetime
from django.utils import timezone


def index(request,receiver_id):
     import pdb
     request.session['receiver_id'] = receiver_id
     message_receiver = User.objects.get(id=request.session['receiver_id'])
     chat_from_user = Message.objects.filter(sender=request.user).filter(receiver=message_receiver)
     chat_from_receiver = Message.objects.filter(sender=message_receiver).filter(receiver=request.user)
     chat = (chat_from_receiver | chat_from_user).order_by('date')
     #pdb.set_trace()
     if request.method == "POST":
          message_instance = Message.objects.create(body=request.POST['chat-msg'], date = datetime.now(),sender = request.user, receiver = message_receiver )
         # chat = Message.objects.filter(sender=request.user).filter(receiver=message_receiver)
     #else:
     #     request.session['receiver_id'] = receiver_id
         # message_receiver = User.objects.get(id=request.session['receiver_id'])
          #chat = Message.objects.filter(sender=request.user).filter(receiver=message_receiver)
     
     return render(request, 'chat_app/index.html', {'chat': chat, 'receiver_id':receiver_id})

@login_required
def home(request):
    users = User.objects.all()
    print(users)
    return render(request, 'chat_app/home.html',{'users':users})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'chat_app/signup.html', {'form': form})
