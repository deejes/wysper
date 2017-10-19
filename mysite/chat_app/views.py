# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,User
from django.shortcuts import render, redirect
from .models import Message 
from datetime import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import MessageSerializer

class MessageList(APIView):
     def get(self,*kwargs):
          sender_id = kwargs[0].user.id
          receiver_id = int(kwargs[1])
          #import pdb; pdb.set_trace()
          user_messages = Message.objects.filter(sender=sender_id).filter(receiver=receiver_id)
          receiver_messages = Message.objects.filter(sender=receiver_id).filter(receiver=sender_id)
          chat = (user_messages | receiver_messages).order_by('date')
          serializer = MessageSerializer(chat,many=True)
          return Response(serializer.data)
     
     def post(self,*kwargs):
          sender_id = User.objects.filter(id=kwargs[0].user.id)[0]
          receiver_id = User.objects.filter(id=int(kwargs[1]))[0]
          # import pdb;pdb.set_trace()
          
          message_instance = Message.objects.create(body=kwargs[0].POST['msgbox'], date = datetime.now(),sender = sender_id, receiver = receiver_id )
          #serializer = MessageSerializer(message_instance,many=True)
          return Response({'created':'yes'})

def chat_box(request,receiver_id):
     # import pdb; pdb.set_trace()
     # request.session['receiver_id'] = receiver_id
     # request.session['pig'] = User.objects.filter(id=receiver_id)[0].username
     # message_receiver = User.objects.get(id=request.session['receiver_id'])
     # chat_from_user = Message.objects.filter(sender=request.user).filter(receiver=message_receiver)
     # chat_from_receiver = Message.objects.filter(sender=message_receiver).filter(receiver=request.user)
     # chat = (chat_from_receiver | chat_from_user).order_by('date')
     # #pdb.set_trace()
     # if request.method == "POST":
     #      message_instance = Message.objects.create(body=request.POST['chat-msg'], date = datetime.now(),sender = request.user, receiver = message_receiver )

     
         # chat = Message.objects.filter(sender=request.user).filter(receiver=message_receiver)
     #else:
     #     request.session['receiver_id'] = receiver_id
         # message_receiver = User.objects.get(id=request.session['receiver_id'])
          #chat = Message.objects.filter(sender=request.user).filter(receiver=message_receiver)
     
     return render(request, 'chat_app/chat_box.html', {'receiver_id':receiver_id})

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
