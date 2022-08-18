"""BlogCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Blog import views as pviews
from mensajeria import views
from django.conf import settings
from django.conf.urls.static import static
from Blog.views import inicio, sobre_mi
from Accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', inicio),
    path('sobre_mi', sobre_mi, name='sobre_mi'),
    path('accounts/', include('Accounts.urls')),
    path('crear_pelicula', pviews.CrearPelicula.as_view(), name='crear_pelicula'),
    path('list_peliculas', pviews.ListadoPost.as_view(), name='list_peliculas'),
    path('mostrar_pelicula/<int:pk>', pviews.MostrarPelicula.as_view(), name='mostrar_pelicula'),
    path('editar_pelicula/<int:pk>', pviews.EditarPelicula.as_view(), name='editar_pelicula'),
    path('eliminar_pelicula/<int:pk>', pviews.EliminarPelicula.as_view(), name='eliminar_pelicula'),
    path('enviar_mensaje', views.EnviarMensaje.as_view(), name='enviar_mensaje'),
    path('listado_mensajes', views.ListadoMensaje.as_view(), name='listado_mensajes'),
    path('mostrar_mensaje/<int:pk>', views.MostrarMensaje.as_view(), name='mostrar_mensaje'),
    path('eliminar_mensaje/<int:pk>', views.EliminarMensaje.as_view(), name='eliminar_mensaje'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)