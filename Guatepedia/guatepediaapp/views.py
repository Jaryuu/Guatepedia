from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import redirect
from models import Investigacion,TablaResultados

import watson
def index(request):
    context = RequestContext(request)

def investigacion(request,nombre_investigacion_url):
    context = RequestContext(request)
    #Sutituyendo _con espacios para construir la investigacion
    nombre_investigacion = nombre_investigacion_url.replace('_',' ')
    investigacion = Investigacion.objects.get(nombre)


# Vista para solicitar aprobacion de investigacion
#Cambia el estado de la investigacion a pendiente de aprobacion
@login_required
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
@login_required
def publicar_investigacion(request,id):
    context = RequestContext(request)

    try:
        inv = Investigacion.objects.get(pk=id)
        inv.estado = 1
        inv.save()
    except Investigacion.DoesNotExist:
        pass

    return HttpResponseRedirect('/admin/guatepediaapp/investigacion')

def buscar(request):
    context = RequestContext(request)
    dict ={}
    if request.method == "POST":
        query = request.POST['param'].strip()
        print(query)
        results = watson.search(query)
        ##Agregando resultados a una tabla HTML
        table = TablaResultados(results)
        dict = {'table' : table}


        for result in results:
            print result.object.contenido

    return render_to_response('guatepediaapp/busqueda.html/',dict,context)