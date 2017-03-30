from django import forms
from mw.apps.mwmain.models import Usuario, Ubicacion, Producto, Categoria

class Form_UsuarioLogin(forms.Form):
	nombreusuario = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class Form_UsuarioAlta(forms.Form):
	nombreusuario = forms.CharField(widget=forms.TextInput())
	# correoelectronico = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))
	password_confirmacion = forms.CharField(widget=forms.PasswordInput(render_value=False))

class Form_UsuarioActualizadInfo(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = '__all__'
		exclude = ['NombreUsuario']
		widgets = {
			"id": forms.TextInput(attrs={'class': 'myfieldclass'})
		}

class Form_AgregarUbicacion(forms.ModelForm):
	class Meta:
		model = Ubicacion
		fields = '__all__'
		exclude = ['idUsuario', 'Estatus']
		widgets = {
			"id": forms.TextInput(attrs={'class': 'myfieldclass'})
		}

class Form_AgregarCategoria(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = '__all__'
		widgets = {
			"id": forms.TextInput(attrs={'class': 'myfieldclass'})
		}

class Form_AgregarProducto(forms.ModelForm):
	class Meta:
		model = Producto
	 	fields = '__all__'
		exclude = ['idUsuario']
		widgets = {
			"id": forms.TextInput(attrs={'class': 'myfieldclass'})
		}