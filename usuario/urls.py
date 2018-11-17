from django.conf.urls import url
from usuario.views import RegistroUsuario, LoginUsuario
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),
]