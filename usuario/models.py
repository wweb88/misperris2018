from django.contrib.auth.models import AbstractUser
from django.db import models

vivienda = (
	('1','Casa con patio grande'),
	('2','Casa con patio pequeño'),
	('3','Casa sin patio'),
	('4','Departamento'),
)

class CustomUser(AbstractUser):
	nombre 		= models.CharField(max_length = 150)
	rut			= models.CharField(max_length = 15)
	nacimiento	= models.DateField()
	telefono	= models.CharField(max_length = 15)
	region		= models.CharField(max_length = 50)
	comuna		= models.CharField(max_length = 50)
	vivienda	= models.CharField(max_length = 50, choices = vivienda, default='1')

	def __str__(self):
		return self.nombre