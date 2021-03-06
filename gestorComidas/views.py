from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Usuario, Preferencias, Menu, Recordatorio
from .formenu import FormMenu
from .formprefer import FormPrefer
from .tasks import proceso_celery
from datetime import datetime
import logging

log = logging.getLogger(__name__) 


def ingreso(request, idUsuario):
	"""
	Iniciar las variables de entorno y validar que tipo de rol tiene el
	usuario para redireccionarlo al template.
	"""
	if request.method == 'GET':
		request.session['idUsuario'] = idUsuario
		request.session['url_slack'] = 'https://nora.cornershop.io'
		menu = Menu.objects.all()
		rol = Usuario.objects.filter(idUsuario=idUsuario).select_related('idRol')
		usr = Usuario.objects.filter(idUsuario=idUsuario)		
		try:
			rol = [data.idRol.nombre for data in rol][0]
			usr = [data.nombre for data in usr][0]
		except Exception as e:
			log.error(f'Error al acceder al rol del usuario {e}')
		if rol == 'admin':
			preferencia = Preferencias.objects.all().select_related('idUsuario')
			recordatorio = Recordatorio.objects.all().select_related('idUsuario')
			template = 'administrador.html'
		else:
			preferencia = Preferencias.objects.filter(idUsuario_id=idUsuario).select_related('idUsuario')
			recordatorio = Recordatorio.objects.filter(idUsuario_id=idUsuario).select_related('idUsuario')
			template = 'usuario.html'

		contexto = {
			'preferencia'  : preferencia,
			'menu'         : menu,
			'recordatorio' : recordatorio,
			'usuario'      : usr
		}
		return render(request, template, contexto)


def crearPreferencia(request):
	"""
	Crea la preferencia del rol usuario pero antes valida que sea antes de las 11am
	"""
	idUsuario = str(request.session['idUsuario'])
	horaActual = datetime.now().time().hour
	res = 'conacceso'
	if horaActual <= 11:
		if request.method == 'GET':
			form = FormPrefer()
		else:
			form = FormPrefer(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(f'../ingresar/{idUsuario}/')
	else:
		form = ''
		res = 'sinacceso'
		log.info('Sin acceso al m??dulo de crear preferencia')
	contexto = {
		'form'  : form,
		'res'   : res
	}	
	return render(request, 'form_crear_prefer.html', contexto)


def crearRecor(request):
	"""
	Enviar un recordatorio de Slack con el men?? de hoy a todos los usuarios
	proceso asincr??nico con celery en la funci??n proceso_celery().
	"""
	idUsuario = str(request.session['idUsuario'])
	url_slack = request.session['url_slack']
	try:
		menu = Menu.objects.latest('idMenu')
	except Exception:
		log.info('No existen menus creados')
		print('No existen menus creados')
	try:
		if request.method == 'GET':
			celery = proceso_celery(menu.menu, url_slack)
			log.info(f'Ejecutando proceso Celery {celery}')
	except Exception as e:
		log.error(f"Error con proceso_celery {e}")
	return HttpResponseRedirect(f'../ingresar/{idUsuario}/')
	

class UsuarioList(ListView):
	"""
	Lista los usuarios para mostrarlos en la pagina de inicio
	"""
	model = Usuario
	template_name = 'index.html'

	def get_queryset(self):
		return self.model.objects.all()


# Menu
class MenuCreate(CreateView):
	"""
	Crea un nuevo menu para el rol admin
	"""
	model = Menu
	form_class = FormMenu
	template_name = 'form_crear.html'
	success_url = reverse_lazy('index')


class MenuUpdate(UpdateView):
	"""
	Edita el menu para el rol admin
	"""
	model = Menu
	form_class = FormMenu
	template_name = 'form_crear.html'
	success_url = reverse_lazy('index')


class MenuDelete(DeleteView):
	"""
	Elimina el menu para el rol admin
	"""
	model = Menu
	form_class = FormMenu
	template_name = 'verificacion_menu.html'
	success_url = reverse_lazy('index')	


# Preferencias
class PreferUpdate(UpdateView):
	"""
	Edita la preferencia para el rol usuario
	"""
	model = Preferencias
	form_class = FormPrefer
	template_name = 'form_crear.html'
	success_url = reverse_lazy('index')


class PreferDelete(DeleteView):
	"""
	Elimina la preferencia para el rol usuario
	"""
	model = Preferencias
	form_class = FormPrefer
	template_name = 'verificacion_prefer.html'
	success_url = reverse_lazy('index')	
