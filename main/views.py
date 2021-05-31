from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users
from .forms import UsersForm
# Create your views here.




def index(request):
    message = Users.objects.order_by('-id')
    return render(request, 'main/index.html', {'message':message})
def chat(request):
    error = ''
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = UsersForm()
    data={
        'form':form,
        'error': error
    }
    return render(request, 'main/chat.html',data)
def chrome(request):
    message = Users.objects.order_by('-id')
    return render(request, 'main/chromeroom.html', {'message':message})
def weather(request):
    message = Users.objects.order_by('-id')
    return render(request, 'main/weatherroom.html', {'message':message})
