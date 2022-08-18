from datetime import date
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Mensaje(models.Model):
    asunto = models.CharField(max_length=50)
    mensaje = RichTextField(blank=True, null=True)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
    destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destino')
    fecha_creacion = models.DateField(default=date.today)

    def __str__(self):
        return self.asunto + ' | ' + str(self.remitente) + ' -> ' + str(self.destino)