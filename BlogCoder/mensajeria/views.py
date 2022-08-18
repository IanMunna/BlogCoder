from django.views.generic import ListView, DetailView, CreateView, DeleteView
from mensajeria.models import Mensaje
from .forms import FormBusquedaMensaje, FormMensaje
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class EnviarMensaje(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = FormMensaje
    success_url = '/listado_mensajes'
    template_name = 'enviar_mensaje.html'


class ListadoMensaje(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'listado_mensajes.html'

    def get_queryset(self):
        asunto = self.request.GET.get('asunto', '')
        if asunto:
            object_list = self.model.objects.filter(asunto__icontains=asunto)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaMensaje()
        return context


class MostrarMensaje(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'mostrar_mensaje.html'


class EliminarMensaje(LoginRequiredMixin, DeleteView):
    model = Mensaje
    template_name = 'eliminar_mensaje.html'
    success_url = '/listado_mensajes'