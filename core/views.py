from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
# Create your views here.

#
# def index(request):
#     return redirect("/agenda")

def listaEvento(request):
    evento = Evento.objects.all()
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)

def eventoLocal(request,titulo_evento):
    data = Evento.objects.filter(titulo = titulo_evento)

    if(len(data) <= 0):
        return HttpResponse('Nenhum Evento Encontrado')
    else:
        return HttpResponse(data[0])