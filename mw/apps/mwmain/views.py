from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from mw.apps.mwmain.models import Usuario, Producto, Ubicacion, Producto
from mw.apps.mwmain.forms import Form_UsuarioLogin, Form_UsuarioAlta, Form_UsuarioActualizadInfo, Form_AgregarUbicacion, Form_AgregarProducto, Form_AgregarCategoria
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def obtener_id(request):
	try:
		current = request.user
		ObjetoUsuario = User.objects.get(id=str(current.id))
		return ObjetoUsuario.id
	except:
		return None

def obtenerObjetoUsuario(request):
	try:
		current = request.user
		ObjetoUsuario = User.objects.get(id=str(current.id))
		return ObjetoUsuario
	except:
		return None

def vista_index(request):
	ctx = None
	try:
		usuario_info = Usuario.objects.get(NombreUsuario=obtener_id(request))
		if usuario_info:
			ctx={"ctx":"mi primera vista", "usuario_info":usuario_info}
		else:
			ctx={"ctx":"usuario_none", "usuario_info":usuario_info}
	except:
		ctx={"ctx":"usuario_none", "usuario_info":None}
	return render_to_response("principal/index.html",ctx, context_instance = RequestContext(request))

def vista_login(request):
	mensaje = ""
	if request.user.is_authenticated():
		ctx = {"ctx":None}
		return HttpResponseRedirect("/")
	else:
		if request.method=="POST":
			forma = Form_UsuarioLogin(request.POST)
			if forma.is_valid():
				username = forma.cleaned_data['nombreusuario']
				password = forma.cleaned_data['password']
				usuario = authenticate(username = username, password = password)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o password incorrecto"
			ctx = {"forma":forma, "ctx":"Inicio de sesion", "mensaje":mensaje}
		else:
			forma = Form_UsuarioLogin()
			ctx = {"forma":forma, "ctx":"No hay inicio de sesion", "mensaje":mensaje}
	return render_to_response("login/login.html",ctx, context_instance=RequestContext(request))

def vista_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def vista_actualizarusuario(request):
	usuario_actualizado = False
	if request.method=="POST":
		forma = Form_UsuarioActualizadInfo(request.POST)
		if forma.is_valid():
			add = forma.save(commit=False)
			current=request.user
			add.NombreUsuario = User.objects.get(username=str(current.username))
			add.save()
			usuario_actualizado = True
			return HttpResponseRedirect('/')
	else:
		usuario_actualizado = False
	forma = Form_UsuarioActualizadInfo()
	ctx = {"usuario_actualizado":usuario_actualizado, "forma":forma}
	return render_to_response("usuario/usuario_actualizar.html",ctx, context_instance=RequestContext(request))

def vista_usuarioalta(request):
	usuario_creado = False
	if request.method=="POST":
		forma = Form_UsuarioAlta(request.POST)
		if forma.is_valid():
			usuario = forma.cleaned_data['nombreusuario']
			password_uno = forma.cleaned_data['password']
			password_dos = forma.cleaned_data['password_confirmacion']
			if password_uno == password_dos:
				ObjUsurario = User.objects.create_user(username=usuario, password=password_uno)
				ObjUsurario.save()
				usuario_creado = True
			else:
				usuario_creado = False
			ctx = {"forma":forma, "usuario_creado":usuario_creado}
			return render_to_response("usuario/usuario_crear.html", ctx, context_instance=RequestContext(request))
		else:
			usuario_creado = False
			ctx = {"forma":forma, "usuario_creado":usuario_creado}
	else:
		usuario_creado = None
		forma = Form_UsuarioAlta()
		ctx = {"forma":forma, "usuario_creado":usuario_creado}
	return render_to_response("usuario/usuario_crear.html", ctx, context_instance=RequestContext(request))

def vista_agregarubicacion(request):
	ubicacion_agregada = False
	if request.method=="POST":
		forma = Form_AgregarUbicacion(request.POST)
		if forma.is_valid():
			try:
				add = forma.save(commit=False)
				current = request.user
				add.idUsuario = User.objects.get(username=str(current.username))
				add.Estatus = True
				add.save()
				ubicacion_agregada = True
			except Exception, e:
				print("except " +str(e))
				forma = Form_AgregarUbicacion()
			ctx = {"forma":forma, "ubicacion_agregada":ubicacion_agregada}
		else:
			forma = Form_AgregarUbicacion()
			ctx = {"forma":forma, "ubicacion_agregada":ubicacion_agregada}
	else:
		forma = Form_AgregarUbicacion()
		ctx = {"forma":forma}
	return render_to_response("ubicacion/ubicacion_crear.html",ctx, context_instance=RequestContext(request))

def vista_verubicaciones(request, id_ubipagina):
	ubicaciones = Ubicacion.objects.filter(idUsuario=obtener_id(request))
	paginator = Paginator(ubicaciones,8)
	try:
		page = int(id_ubipagina)
	except:
		page = 1

	try:
		ubucacinesNum = paginator.page(page)
	except (EmptyPage, InvalidPage):
		ubucacinesNum = paginator.page(paginator.num_pages)

	ctx= {"ubicaciones":ubucacinesNum}
	return render_to_response("ubicacion/ubicacion_ver.html",ctx, context_instance=RequestContext(request))

def vista_verubicacion_sencilla(request, id_ubicacion):
	ubicacion = Ubicacion.objects.get(id=id_ubicacion)
	productos_xubicacion = Producto.objects.filter(idUbicacion=id_ubicacion)
	ctx = {"ubicacion":ubicacion, "productos":productos_xubicacion}
	return render_to_response("ubicacion/ubicacion_ver_sencilla.html",ctx, context_instance=RequestContext(request))

def vista_productos_ver(request):
	productos = Producto.objects.filter(id=obtener_id(request))
	ctx = {"productos":productos}
	return render_to_response("producto/productos_ver.html",ctx, context_instance=RequestContext(request))

def vista_agregarcategoria(request):
	if request.method == "POST":
		forma = Form_AgregarCategoria(request.POST)
		if forma.is_valid():
			try:
				forma.save()
				categoria_agregada = True
			except:
				categoria_agregada = False
		else:
			categoria_agregada = False
		forma = Form_AgregarCategoria()
		ctx = {"categoria_agregada":categoria_agregada, "forma":forma}
	else:
		categoria_agregada = False
		forma = Form_AgregarCategoria()
		ctx = {"categoria_agregada":categoria_agregada, "forma":forma}
	return render_to_response("categoria/categoria_agregar.html",ctx, context_instance=RequestContext(request))

def vista_agregarproductos(request, id_ProdUbicacion):
	producto_agregado = False
	if request.method=="POST":
		forma = Form_AgregarProducto(request.POST)
		if forma.is_valid():
			add = forma.save(commit=False)
			current = request.user
			add.idUsuario = User.objects.get(username=str(current.username))
			add.idCategoria = forma.cleaned_data['idCategoria']
			add.idUbicacion = forma.cleaned_data['idUbicacion']
			add.save()
			producto_agregado= True
	else:
		forma = Form_AgregarProducto()
	ctx = {"forma":forma,"idUbicacion":id_ProdUbicacion,"producto_agregado":producto_agregado}
	return render_to_response("producto/productos_agregar.html",ctx, context_instance=RequestContext(request))