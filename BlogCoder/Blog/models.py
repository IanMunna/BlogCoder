from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Pelicula(models.Model):
    titulo=models.CharField(max_length=30)
    trama=RichTextField(null=True)
    fecha_estreno=models.DateField(auto_now_add=True, null=True , blank=True)
    imagen=models.ImageField(upload_to='imagenes', null=True, blank=True)
    director=models.CharField(max_length=30, null=True)
    
    def _str_(self):
        return f'Titulo: {self.titulo} - Fecha estreno: {self.fecha_estreno} - Creado por {self.director}'
        