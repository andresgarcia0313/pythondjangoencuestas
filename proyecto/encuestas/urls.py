from django.urls import path
from . import views
urlpatterns =[
	#ejemplo /encuestas/
	path('',views.index,name='index'),
	#ejemplo /encuestas/5/
	path ('<int:pregunta_id>/', views.detalle, name='detalle'),
	#ejemplo /encuestas/5/resultados
	path('<int:pregunta_id>/resultados/',views.resultados, name='resultados'),
	#ejemplo /encuestas/5/voto/
	path('<int:pregunta_id>/voto/', views.voto, name='voto'),
]
