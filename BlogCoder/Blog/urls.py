from django.urls import path
from . import views
from .views import inicio, sobre_mi

urlpatterns = [
    path('', inicio, name= 'index'),
    path('about/', sobre_mi, name='sobre_mi'),
    path('peliculas/', views.ListPeliculas.as_view(), name='listado_peliculas'),
    path('crear_pelicula/', views.CrearPelicula.as_view(), name='crear_pelicula'),
    path('editar_pelicula/<int:pk>/', views.EditarPelicula.as_view(), name='editar_pelicula'),
    path('eliminar_pelicula/<int:pk>/', views.EliminarPelicula.as_view(), name='eliminar_pelicula'),
    path('peliculas/<int:pk>/', views.MostrarPelicula.as_view(), name='mostrar_pelicula'),
]