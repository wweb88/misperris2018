from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mascota.forms import MascotaForm
from .models import Mascota


# Create your views here.

class index(ListView):
	model = Mascota
	template_name = 'masota_list.html'


class mascota_new(CreateView):
	model =	Mascota
	form_class = MascotaForm
	template_name = 'mascota\mascota_form.html'
	success_url = reverse_lazy('index')


class mascota_edit(UpdateView):
	model =	Mascota
	form_class = MascotaForm
	template_name = 'mascota\mascota_form.html'
	success_url = reverse_lazy('index')

class mascota_delete(DeleteView):
	model =	Mascota
	template_name = 'mascota\mascota_delete.html'
	success_url = reverse_lazy('index')

class mascota_adoptar(UpdateView):
	model =	Mascota
	form_class = MascotaForm
	template_name = 'mascota\mascota_adoptar.html'
	success_url = reverse_lazy('index')