from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
# Create your views here.

#
# def index(request):
#     return redirect("/agenda")
def login_user(request):
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("/")

def submit_login(request):
    if(request.POST):
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if(usuario is not None):
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, message="Usuário ou senha inválido")

        return redirect('/')

@login_required(login_url="/login/")
def listaEvento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)


@login_required()
def eventoLocal(request,titulo_evento):
    data = Evento.objects.filter(titulo = titulo_evento)

    if(len(data) <= 0):
        return HttpResponse('Nenhum Evento Encontrado')
    else:
        return HttpResponse(data[0])