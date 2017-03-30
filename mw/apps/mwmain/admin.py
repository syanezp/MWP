from django.contrib import admin
from mw.apps.mwmain.models import Usuario, Categoria, Producto, Ubicacion, Cuenta

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Ubicacion)
admin.site.register(Cuenta)