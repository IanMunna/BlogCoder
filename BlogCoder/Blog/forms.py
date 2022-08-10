from socket import fromshare
from django import forms
from ckeditor.fields import RichTextFormField

class PeliculaF(forms.Form):
    titulo=forms.CharField(max_length=30)
    trama=RichTextFormField()
    fecha_estreno=forms.DateField(required=False)
    imagen=forms.ImageField(required=False)
    director=forms.CharField(max_length=30)

class BusquedaPelicula(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
    
