# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,User
from django.shortcuts import render, redirect
from .models import Message 
from datetime import datetime


def index(request,receiver_id):
     import pdb

     pdb.set_trace()
     request.session['receiver_id'] = receiver_id
     if request.method == "POST":
          message_instance = Message.objects.create(body=request.POST['chat-msg'])
     return render(request, 'chat_app/index.html')

def test(request):
    import pdb
    #pdb.set_trace()
    if request.method == "POST":
          message_instance = Message.objects.create(body=request.POST['chat-msg'], date = datetime.now(),sender = request.user, receiver = User.objects.filter(id=request.session['receiver_id'])[0] )     
    messes = Message.objects.all
    mes = request.POST['chat-msg']
    return render(request, 'chat_app/test.html', {'mes':mes,'messes':messes})

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
