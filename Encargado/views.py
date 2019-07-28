from django.shortcuts import render, HttpResponseRedirect, redirect,reverse
import datetime
from Core.models import Horario,Persona,Mensaje,Grupo,Mensajeria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from Encargado.forms import UserForm
from django.contrib import messages
import datetime
# Create your views here.

def Index_Encargado(request):
	persona = Persona.objects.get(Usuario = request.user)
	if(persona.Tipo == "EN"):
		return render(request,"Encargado/index.html",{})
	else:
		return redirect(reverse('Index'))

def Listar_Grupos(request):
	data = {}
	encargado = Persona.objects.get(Usuario = request.user)
	grupos = Grupo.objects.filter(Encargado = encargado)
	data["grupo"] = grupos
	return render(request,"Encargado/listar_grupos.html",data)

def Agregar_Grupo(request):
	data = {}
	return render(request,"Encargado/listar_perfil.html",data)
def Ver_Perfiles_Horario(request):
	data = {}
	personas = Persona.objects.filter(Tipo="TR")
	paginator = Paginator(personas, 2)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	data["contacts"] = contacts
	return render(request,"Encargado/ver_perfiles_horario.html",data)

def Ver_Horario(request,pk):
	data = {}
	persona = Persona.objects.get(pk = pk)
	horario = Horario.objects.filter(Usuario = persona)
	paginator = Paginator(horario, 15)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	data["contacts"] = contacts
	data["pk"] = pk
	return render(request,"Encargado/ver_horario.html",data)

def Nueva_Tarea_Encargado(request,pk):
	if request.method == "POST":

		new_h = Horario()
		new_h.Mensaje = request.POST["Mensaje"]
		new_h.Usuario = Persona.objects.get(pk = pk)
		new_h.save()
		return redirect(Ver_Horario,pk)

def Ver_Mensajes(request):
	data = {}
	usuario = User.objects.get(username = request.user)
	mensajes_e = Mensajeria.objects.filter(Emisor__Usuario=usuario)
	mensajes_r = Mensajeria.objects.filter(Receptor__Usuario=usuario)

	total_mensajes = list(mensajes_e) + list(mensajes_r)
	total_usuarios = []
	personas = Persona.objects.filter(Usuario__is_staff=False)
	data["personas"] = personas
	for i in total_mensajes:
		if((i.Emisor in total_usuarios) == False):
			total_usuarios.append(i.Emisor)
	mensajes_enviar = []

	for i in total_usuarios:
		mensajes = list(Mensajeria.objects.filter(Emisor__Usuario=usuario)) + list(Mensajeria.objects.filter(Receptor__Usuario=usuario))
		fecha_aux = mensajes[0].Fecha
		mensaje_aux = mensajes[0]
		for i in mensajes:
			if fecha_aux < i.Fecha:
				mensaje_aux = i
				fecha_aux = i.Fecha
		mensajes_enviar.append(mensaje_aux)

	paginator = Paginator(mensajes_enviar, 15)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	data["contacts"] = contacts
	return render(request,"Encargado/ver_mensajes.html",data)

def Chat(request,pk):
	usuario = User.objects.get(username = request.user)
	trabajador = Persona.objects.get(pk = pk)
	data = {}
	mensajes = list(Mensajeria.objects.filter(Emisor__Usuario=usuario,Receptor = trabajador)) + list(Mensajeria.objects.filter(Receptor__Usuario=usuario, Emisor=trabajador))
	data["mensajes"] = mensajes
	data["chatis"] = trabajador
	data["pk"] = pk
	return render(request,"Encargado/foro.html",data)

def Nuevo_Mensaje_Encargado(request,pk):
	if request.method == "POST":
		new_m = Mensajeria()
		new_m.Mensaje = request.POST["Mensaje"]
		new_m.Receptor = Persona.objects.get(pk = pk)
		new_m.Emisor = Persona.objects.get(Usuario = request.user)
		new_m.save()
		return JsonResponse({})

def Enviar_Mensaje(request):
	if request.method == "POST":
		usuario = User.objects.get(username = request.user)
		receptor = Persona.objects.get(pk = request.POST["receptor_pk"])
		new_m = Mensajeria()
		new_m.Emisor = Persona.objects.get(Usuario = usuario)
		new_m.Receptor = receptor
		new_m.Mensaje = request.POST["mensaje"]
		new_m.save()
		return redirect(Mensajeria)
	return redirect("Ver_Mensajes")

def Gestionar_Perfil(request):
	template_name = 'Encargado/listar_perfil.html'
	page = request.GET.get('page')
	contact_list = []
	personas = Persona.objects.all()
	users = []
	for i in personas:
		users.append(i.Usuario)
	paginator = Paginator(users, 15)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	data = {}
	data['contacts'] =contacts
	data['form'] = UserForm()
	if request.method == "POST":
		data['form'] = UserForm(request.POST, request.FILES)
		if(data['form'].is_valid()):
			if(request.POST["password1"] == request.POST["password2"]):
				if(len(request.POST["password1"]) >= 8):
					user = User.objects.create_user(username=request.POST["username"],password= request.POST["password1"])
					user.save()
					new_persona = Persona()
					new_persona.Usuario = user
					new_persona.Tipo = 'TR'
					new_persona.save()
					
					return redirect('Gestionar_Perfil')
				else:
					messages.warning(
	                request,
	                'El largo de la contraseña debe ser mayor a 8'
	            	)
			else:
				messages.error(
                request,
                'Las contraseñas no coinsiden'
            	)
			
		else:
			data['form'] = UserForm()
			messages.error(
                request,
                'La Contraseña es Similar al Nombre de Usuario'
            )

	return render(request, template_name,data)
