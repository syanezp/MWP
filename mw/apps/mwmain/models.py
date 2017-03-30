from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
	NombreUsuario = models.OneToOneField(User)
	Email = models.EmailField(max_length=100)
	# Password = models.CharField(max_length=64)	
	Nombre = models.CharField(max_length=80)
	Apellido = models.CharField(max_length=80)
	Direccion = models.CharField(max_length=200)
	Telefono = models.CharField(max_length=12)
	FechaNacimiento = models.DateField(auto_now_add=False)
	Ciudad = models.CharField(max_length=50)
	Estado = models.CharField(max_length=50)
	CP = models.CharField(max_length=5)
	FechaAlta = models.DateField(auto_now_add=True)
	Rol = models.BooleanField("Cliente?",default=False)
	Activo = models.BooleanField("Estatus", default=True)
	Suscripcion = models.BooleanField("Suscripcion", default=False)
	Fotografia = models.ImageField(upload_to="images/usuarios", null=True, blank=True)

	def __str__(self):
		return "%s %s" % (self.Nombre, self.Apellido)

class Categoria(models.Model):
	Nombre = models.CharField(max_length=50)
	Descripcion = models.TextField(max_length=200)

	def __str__(self):
		return "%s" % (self.Nombre)

class Ubicacion(models.Model):
	idUsuario = models.ForeignKey(User,null=False,blank=False)
	Nombre = models.CharField(max_length=50)
	Descripcion = models.TextField(max_length=200)
	Latitud = models.CharField(max_length=10)
	Longitud = models.CharField(max_length=10)
	Estatus = models.BooleanField("Esta ubucacion aun esta activa?", default=True)
	Fotografia = models.ImageField(upload_to="images/ubicaciones", null=True, blank=True)

	def __str__(self):
		return "%s" % (self.Nombre)

class Producto(models.Model):
	idUsuario = models.ForeignKey(User,null=False,blank=False)
	idCategoria = models.ForeignKey(Categoria,null=True,blank=True)	
	idUbicacion = models.ForeignKey(Ubicacion,null=True,blank=True)
	Nombre = models.CharField(max_length=50)
	Descripcion = models.TextField(max_length=200)
	Precio = models.IntegerField(blank=True, null=True)
	Estatus = models.BooleanField("Estatus del producto", default=True)
	Fotografia = models.ImageField(upload_to="images/productos", null=True, blank=True)

	def __str__(self):
		return "%s" % (self.Nombre)

class Cuenta(models.Model):
	idUsuario = models.ForeignKey(User,null=False,blank=False)
	FechaPago = models.DateField()
	NumTarjeta = models.CharField(max_length=19)
	Pago = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return "%s" % (self.FechaPago)