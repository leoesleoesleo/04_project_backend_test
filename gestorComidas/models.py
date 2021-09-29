from django.db import models

class Rol(models.Model):
	idRol = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	
class Usuario(models.Model):
	idUsuario = models.AutoField(primary_key=True)
	idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
	cedula = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=150)
	correo = models.CharField(max_length=100)

class Recordatorio(models.Model):
	idRecord = models.AutoField(primary_key=True)
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
	fecha = models.CharField(max_length=100)
	url = models.CharField(max_length=100)

class Menu(models.Model):
	idMenu = models.AutoField(primary_key=True)
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
	menu = models.CharField(max_length=200)
	fecha = models.CharField(max_length=200)

class Preferencias(models.Model):
	idPrefer = models.AutoField(primary_key=True)
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
	preferencia = models.CharField(max_length=200)
	personaliza = models.CharField(max_length=200)
	fecha = models.CharField(max_length=200)
