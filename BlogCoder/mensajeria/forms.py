from django import forms
from .models import Mensaje


class FormMensaje(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('asunto', 'mensaje', 'remitente', 'destino', 'fecha_creacion')
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
            'remitente': forms.Select(attrs={'id': 'autor'}),
            'destino': forms.Select(attrs={'class': 'form-control'}),
            'fecha_creacion': forms.DateInput(attrs={'id': 'fecha'}),
        }


class FormBusquedaMensaje(forms.Form):
    asunto = forms.CharField(max_length=50, required=False)
