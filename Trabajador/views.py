from django.shortcuts import render, HttpResponseRedirect, redirect,reverse
import datetime
from Core.models import Horario,Persona,Mensaje,Mensajeria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
# Create your views here.

def Index(request):
	return render(request,"index.html",{})

def Mensajeria_Trabajador(request):
	mensajes = Mensajeria.objects.all()
	data = {}
	data["mensajes"] = mensajes
	return render(request,"foro.html",data)

def Nuevo_Mensaje(request):
	if request.method == "POST":
		new_m = Mensajeria()
		new_m.Mensaje = request.POST["Mensaje"]
		new_m.Emisor = Persona.objects.get(Usuario = request.user)
		new_m.Receptor = Persona.objects.get(pk = 2)
		new_m.save()
		return redirect(Mensajeria_Trabajador)

def Horario_Semana(request):
	return render(request,"horario.html",{})

def Cuentionario(request):
	return render(request,"Cuestionario.html",{})

def Tareas(request,dia):
	data = {}
	date = datetime.date.today()
	semana = date.weekday()
	fecha = date - datetime.timedelta(days= abs(dia - semana))
	horario = Horario.objects.filter(Fecha__day = fecha.day,Fecha__month = fecha.month, Fecha__year=fecha.year)
	paginator = Paginator(horario, 15)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	data['contacts'] = contacts
	data["dia"] = dia
	return render(request,"tareas.html",data)

def Nueva_Tarea(request):
	if request.method == "POST":

		new_h = Horario()
		new_h.Mensaje = request.POST["Mensaje"]
		new_h.Usuario = Persona.objects.get(Usuario = request.user)
		new_h.save()
		return redirect(Tareas,5)

def Ver_Companeros(request):
	return render(request,"companeros.html",{})