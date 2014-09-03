from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import redirect
from models import Investigacion

def index(request):
    context = RequestContext(request)
    response = "Hello, world. You're at the polls index."
    return HttpResponse(response)

def home(request):
    return HttpResponse("Homepage")

def investigacion(request,nombre_investigacion_url):
    context = RequestContext(request)
    #Sutituyendo _con espacios para construir la investigacion
    nombre_investigacion = nombre_investigacion_url.replace('_',' ')
    investigacion = Investigacion.objects.get(nombre)

def mostrarInvestigacion(request,id):
    context = RequestContext(request)
    inv=None
    try:
            inv = Investigacion.objects.get(pk=id)
    except Investigacion.DoesNotExist:
        pass
    return HttpResponse(inv)


# Vista para solicitar aprobacion de investigacion
#Cambia el estado de la investigacion a pendiente de aprobacion
def solicitar_aprobacion(request,id):
    context = RequestContext(request)

    if(request.method=='GET'):
        #Obteniendo Investigacion en base a la id
        try:
            inv = Investigacion.objects.get(pk=id)
            inv.estado = 5
            inv.save()
        except Investigacion.DoesNotExist:
            pass
    return HttpResponseRedirect('/admin/guatepediaapp/investigacion/')

def publicar_investigacion(request,id):
    context = RequestContext(request)

    try:
        inv = Investigacion.objects.get(pk=id)
        inv.estado = 1
        inv.save()
    except Investigacion.DoesNotExist:
        pass

    return HttpResponseRedirect('/admin/guatepediaapp/investigacion')
