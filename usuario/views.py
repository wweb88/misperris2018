from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

# Create your views here.

class RegistroUsuario(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('home')
	template_name = 'usuario/registrar.html'


class LoginUsuario(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('home')
	template_name = 'usuario/registrar.html'