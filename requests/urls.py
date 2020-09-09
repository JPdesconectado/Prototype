from django.urls import path
from . import views

urlpatterns = [
	path('', views.inicio, 									name = 'inicio'),
    path('solicitacao/', views.lista_solicitacao,			name = 'lista_solicitacao'),
    path('solicitacao/<int:pk>/',views.detalhe_solicitacao, name = 'detalhe_solicitacao'),
    path('solicitacao/nova/', views.nova_solicitacao,		name = 'nova_solicitacao'),
    path('solicitacao/<int:pk>/editar_status/', views.editar_status,	name = 'editar_status'),
]