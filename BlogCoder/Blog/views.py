from django.shortcuts import render, redirect
from .forms import BusquedaPelicula, PeliculaF
from .models import Pelicula
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio(request):
    return render(request, 'base.html')

@login_required
def sobre_mi(request):
    return render(request, 'sobre_mi.html')

class ListPeliculas(ListView):
    model=Pelicula
    template_name= 'list_peliculas.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo: 
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaPelicula()
        return context

class CrearPelicula(LoginRequiredMixin, CreateView):
    model=Pelicula
    template_name= 'crear_pelicula.html'
    success_url= '/peliculas'
    fields= ['titulo', 'trama', 'imagen']
    form_class: PeliculaF
    def form_valid(self, form):
        user= User.objects.get(username= self.request.user)
        Pelicula.objects.create(titulo= self.request.POST['titulo'], trama= self.request.POST['trama'], imagen= self.request.Files['imagen'], director= user)
        return redirect(self.success_url)

class EditarPelicula(LoginRequiredMixin, UpdateView):
    model=Pelicula
    template_name = 'editar_pelicula.html'
    success_url = '/peliculas'
    fields = ['titulo', 'trama', 'imagen']


class EliminarPelicula(LoginRequiredMixin, DeleteView):
    model=Pelicula
    template_name = 'eliminar_pelicula.html'
    success_url = '/pelicula'


class MostrarPelicula(DetailView):
    model = Pelicula
    template_name = 'mostrar_pelicula.html'


