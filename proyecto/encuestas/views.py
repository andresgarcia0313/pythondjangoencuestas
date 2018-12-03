#from django.shortcuts import render
from django.http import HttpResponse
from .models import Pregunta
# Create your views here.


# ejemplo de manejo simple de solicitud de url
'''
def index(request):
	return HttpResponse("Bienvenido a las encuestas")
'''
def detalle(request, pregunta_id):
	return HttpResponse("Estas mirando la pregunta %s." % pregunta_id)
def resultados(request, pregunta_id):
	response = "Estas viendo los resultados de la pregunta %s."
	return HttpResponse(response % pregunta_id)
def voto(request, pregunta_id):
	return HttpResponse("Estas Votando en la pregunta %s." % pregunta_id)

def index (request):
	lista_ultimas_preguntas=Pregunta.objects.order_by('-fecha_de_publicacion')[:5]
	salida=', '.join([p.pregunta_text for q in lista_ultimas_preguntas])
	return HttpResponse(salida)
