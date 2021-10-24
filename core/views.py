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
        else:
            messages.error(request, message="Usuário ou senha inválido")

        return redirect('/')

@login_required(login_url="/login/")
def listaEvento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)


@login_required(login_url="/login/")
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url="/login/")
def submit_evento(request):
    if(request.POST):
        titulo      = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao   = request.POST.get('descricao')
        local       = request.POST.get('local')
        usuario     = request.user

        Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, local=local, usuario=usuario)


    return redirect('/')


@login_required(login_url="/login/")
def eventoLocal(request,titulo_evento):
    data = Evento.objects.filter(titulo = titulo_evento)

    if(len(data) <= 0):
        return HttpResponse('Nenhum Evento Encontrado')
    else:
        return HttpResponse(data[0])