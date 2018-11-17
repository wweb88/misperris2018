from django import forms
from mascota.models import Mascota


estado = (
	('rescatado','Rescatado'),
	('disponible','Disponible'),
	('adoptado','Adoptado'),
)

class MascotaForm(forms.ModelForm):
	class Meta:
		model = Mascota

		fields = [
			'imagen',
			'nombre',
			'raza',
			'estado',
			'descripcion',
			'persona',
		]
		labels = {
			'imagen' : 'Imagen',
			'nombre' : 'Nombre',
			'raza' : 'Raza',
			'estado' : 'Estado',
			'descripcion' : 'Descripción',
			'persona' : 'Adoptante',
		}
		widgets = {
			'imagen': forms.FileInput(attrs={'class' : 'form-control'}),
			'nombre': forms.TextInput(attrs={'class' : 'form-control'}),
			'raza': forms.TextInput(attrs={'class' : 'form-control'}),
			'estado': forms.Select(choices = estado,attrs={'class' : 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class' : 'form-control'}),
			'persona': forms.TextInput(attrs={'class' : 'form-control'}),
		}