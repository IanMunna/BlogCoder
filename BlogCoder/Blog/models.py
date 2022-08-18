from datetime import date
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    subtitulo = models.CharField(max_length=50, null=True)
    contenido = RichTextUploadingField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=date.today)
    imagen = models.ImageField(upload_to="imagenes_de_pelicula/")

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('mostrar_pelicula', args=(str(self.id)))