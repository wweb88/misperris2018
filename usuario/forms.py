from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


vivienda = (
	('1','Casa con patio grande'),
	('2','Casa con patio pequeño'),
	('3','Casa sin patio'),
	('4','Departamento'),
)

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = [
			'username',
			'email',
			'nombre',
			'rut',
			'nacimiento',
			'telefono',
			'region',
			'comuna',
			'vivienda',
		]
		labels = {
			'username' : 'Nombre de Usuario',
			'email' : 'Email',
			'nombre' : 'Nombre',
			'rut' : 'Rut',
			'nacimiento' : 'Fecha de Nacimiento',
			'telefono' : 'Teléfono',
			'region' : 'Región',
			'comuna' : 'Comuna',
			'vivienda' : 'Tipo de Vivienda',
		}
		widgets = {
			'username' : forms.TextInput(attrs={'class' : 'form-control'}),
			'email' : forms.TextInput(attrs={'class' : 'form-control'}),
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'rut' : forms.TextInput(attrs={'class' : 'form-control'}),
			'nacimiento' : forms.TextInput(attrs={'class' : 'form-control'}),
			'telefono' : forms.TextInput(attrs={'class' : 'form-control'}),
			'region' : forms.TextInput(attrs={'class' : 'form-control'}),
			'comuna' : forms.TextInput(attrs={'class' : 'form-control'}),
			'vivienda' : forms.Select(choices = vivienda,attrs={'class' : 'form-control'}),
		}



class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'email')