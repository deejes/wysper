# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,User
from django.shortcuts import render, redirect




def index(request):
     return render(request, 'chat_app/index.html')

def test(request):
     
     import pdb
     pdb.set_trace()
     mes = request.POST['chat-msg']
     return render(request, 'chat_app/test.html', {'mes':mes})

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
