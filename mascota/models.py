from django.db import models
from usuario.models import CustomUser

estado = (
	('rescatado','Rescatado'),
	('disponible','Disponible'),
	('adoptado','Adoptado'),
)

# Create your models here.
class Mascota(models.Model):
	imagen 		= models.ImageField(default='default.png', blank=True)
	nombre 		= models.CharField(max_length = 100)
	raza 		= models.CharField(max_length = 50)
	estado		= models.CharField(max_length = 50, choices = estado, default='rescatado')
	descripcion	= models.CharField(max_length = 300)
	persona		= models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre