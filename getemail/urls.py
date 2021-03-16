from django.urls import path
from . import views

urlpatterns = [
	path('resposta/', views.lista_resposta, name = 'lista_resposta'),
	path('resposta/<int:pk>/', 					views.detalhe_resposta, 		name = 'detalhe_resposta'),
]