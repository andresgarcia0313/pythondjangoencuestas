import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# https://docs.djangoproject.com/es/2.1/intro/tutorial02/


class Pregunta(models.Model):
    texto_de_la_pregunta = models.CharField(max_length=200)
    fecha_de_publicacion = models.DateTimeField()

    def __str__(self):
        return self.texto_de_la_pregunta

    def fue_publicado_recientemente(self):
        return self.fecha_de_publicacion >= timezone.now() - datetime.timedelta(days=1)


class Eleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_de_eleccion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_de_eleccion


'''
Jugando con la api
1. Ingresar a la api
    Python manage.py shell
2. Importar las clases modelo escritas
    from encuestas.models import Pregunta, Eleccion
    from django.utils import timezone
3. Listar Objetos Creados 
    Pregunta.objects.all()
4. Crea un objeto o lo instancia de forma temporal del modelo 
    p = Pregunta(texto_de_la_pregunta = "¿Qué hay de nuevo?", fecha_de_publicacion = timezone.now())
5. Almacenar el objeto en memoria fija (base de datos)
    p.save()
6. Después de almacenarlo el objeto se le asigna id
    p.id
    p.texto_de_la_pregunta
    p.fecha_de_publicacion
7. Modifiquemos un atributo
    p.texto_de_la_pregunta = "¿Qué Pasa?"
    p.save()
8.  Consultando los objetos
        Pregunta.objects.all()
        Nos mostrara <QuerySet [<Pregunta: Pregunta object (1)>]>
    Cambiemos el metodo para que nos muestre el texto 
    sobreescritura del método __str__() a los modelos ejemplo
    def __str__(self):
        return self.texto_de_la_pregunta
9. Iniciar un nuevo Shell como punto 1
10. Consultar nuestras Preguntas Como el punto 2 y el 3
11. Django proporciona una API de búsqueda de base de datos
    enriquecida que está completamente controlada por argumentos de palabras clave.
    Pregunta.objects.filter(id=1)
12. Busqueda por texto
    Pregunta.objects.filter(texto_de_la_pregunta__startswith='¿Qué')
13. Consultar las preguntas del anio actual
    from django.utils import timezone
    anio_actual = timezone.now().year
    Pregunta.objects.get(fecha_de_publicacion__year=anio_actual)
14. Solicite una ID inexiste, genera excepción
    Pregunta.objects.get(id=2)
15. Atajo de busqueda por id
    Question.objects.get(pk=1)
16. Asegúrar que método personalizado funciono.
    Creamos el objeto a partir de su id
    p = Pregunta.objects.get(pk=1)
    p.fue_publicado_recientemente()
17. Asignar varias opciones de elección a unica pregunta
    Consultemos las preguntas asociadas 
    q.eleccion_set.all()
'''