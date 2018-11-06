from django.db import models
# Create your models here.
# https://docs.djangoproject.com/es/2.1/intro/tutorial02/


class Pregunta(models.Model):
    texto_de_la_pregunta = models.CharField(max_length=200)
    fecha_de_publicacion = models.DateTimeField()


class Eleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_de_eleccion = models.CharField(max_length=200)
    votos=models.IntegerField(default=0)