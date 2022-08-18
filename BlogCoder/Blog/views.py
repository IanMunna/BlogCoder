from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Blog.models import Pelicula
from .forms import FormBusquedaPelicula, FormPelicula
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ListadoPost(ListView):
    model = Pelicula
    template_name = 'list_peliculas.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaPelicula()
        return context

def inicio(request):

    ultimos_diez_peliculas = Pelicula.objects.all().order_by('-id')[:10]

    return render(request, 'index.html', {'list_peliculas': ultimos_diez_peliculas[:3], 'ultimos_diez': ultimos_diez_peliculas})


def sobre_mi(request):
    return render(request, 'sobre_mi.html')

class CrearPelicula(LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = FormPelicula
    success_url = '/list_peliculas'
    template_name = 'crear_pelicula.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditarPelicula(LoginRequiredMixin, UpdateView):
    model = Pelicula
    form_class = FormPelicula
    success_url = '/list_peliculas'
    template_name = 'editar_pelicula.html'


class EliminarPelicula(LoginRequiredMixin, DeleteView):
    model = Pelicula
    template_name = 'eliminar_pelicula.html'
    success_url = '/list_peliculas'


class MostrarPelicula(DetailView):
    model = Pelicula
    template_name = 'mostrar_pelicula.html'