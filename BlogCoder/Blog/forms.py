from django import forms
from .models import Pelicula

class FormPelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'subtitulo', 'contenido', 'autor', 'fecha_creacion', 'imagen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'id': 'autor'}),
            'fecha_creacion': forms.DateInput(attrs={'id': 'fecha'}),
        }


class FormBusquedaPelicula(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)
    
