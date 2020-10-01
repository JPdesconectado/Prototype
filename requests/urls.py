from django.urls import path
from . import views

urlpatterns = [

	path('', 												views.inicio, 								name = 'inicio'),

    path('solicitacao_transito/', 							views.lista_solicitacao_transito,			name = 'lista_solicitacao_transito'),
    path('solicitacao_transito/<int:pk>/', 					views.detalhe_solicitacao_transito, 		name = 'detalhe_solicitacao_transito'),
    path('solicitacao_transito/nova/', 						views.nova_solicitacao_transito,			name = 'nova_solicitacao_transito'),

    path('solicitacao_educacao/',							views.lista_solicitacao_educacao,			name = 'lista_solicitacao_educacao'),
    path('solicitacao_educacao/<int:pk>/',					views.detalhe_solicitacao_educacao,			name = 'detalhe_solicitacao_educacao'),
    path('solicitacao_educacao/nova/', 						views.nova_solicitacao_educacao, 			name = 'nova_solicitacao_educacao'),

    path('solicitacao_iluminacao/',							views.lista_solicitacao_iluminacao,			name = 'lista_solicitacao_iluminacao'),
    path('solicitacao_iluminacao/<int:pk>/',				views.detalhe_solicitacao_iluminacao,		name = 'detalhe_solicitacao_iluminacao'),
    path('solicitacao_iluminacao/nova/', 					views.nova_solicitacao_iluminacao, 			name = 'nova_solicitacao_iluminacao'),

    path('solicitacao_upa/',                               views.lista_solicitacao_upa,                 name = 'lista_solicitacao_upa'),
    path('solicitacao_upa/<int:pk>/',                      views.detalhe_solicitacao_upa,               name = 'detalhe_solicitacao_upa'),
    path('solicitacao_upa/nova/',                          views.nova_solicitacao_upa,                  name = 'nova_solicitacao_upa'),

    path('solicitacao/<int:pk>/editar_status/', 			views.editar_status,						name = 'editar_status'),
]