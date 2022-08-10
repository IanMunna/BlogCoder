from django.shortcuts import render
from .forms import BusquedaPelicula, PeliculaF
from .models import Pelicula
from datetime import datetime

# Create your views here.

def inicio(request):
    return render(request, 'main.html')

