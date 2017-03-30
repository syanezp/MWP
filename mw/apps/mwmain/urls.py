from django.conf.urls import patterns, include, url

urlpatterns = patterns('mw.apps.mwmain.views',
	url(r'^$', "vista_index",name="index"),
	url(r'^login/$', "vista_login",name="vista_login"),
	url(r'^logout/$', "vista_logout",name="vista_logout"),
	url(r'^usuario_actualizar/$', "vista_actualizarusuario",name="vista_actualizarusuario"),
	url(r'^usuario_crear/$', "vista_usuarioalta",name="vista_crearusuario"),
	url(r'^ubicacion_ver/page/(?P<id_ubipagina>.*)/$', "vista_verubicaciones",name="vista_verubicacion"),
	url(r'^ubicacion_single/(?P<id_ubicacion>\d+)/$', "vista_verubicacion_sencilla",name="vista_verubicacion_sencilla"),
	url(r'^ubicacion_crear/$', "vista_agregarubicacion",name="vista_crearubicacion"),
	url(r'^productos_ver/$', "vista_productos_ver",name="vista_productosver"),
	url(r'^productos_agregar/(?P<id_ProdUbicacion>\d+)$', "vista_agregarproductos",name="vista_productosagregar"),
	url(r'^categoria_agregar/$', "vista_agregarcategoria",name="vista_categoriaagregar"),
)

# url(r'^ubicacion_ver/$', "vista_verubicaciones",name="vista_verubicacion"),