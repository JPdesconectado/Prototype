from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

	path('', 												views.inicio, 								name = 'inicio'),
    # Transito
    path('solicitacao_transito/', 							views.lista_solicitacao_transito,			name = 'lista_solicitacao_transito'),
    path('solicitacao_transito/<int:pk>/', 					views.detalhe_solicitacao_transito, 		name = 'detalhe_solicitacao_transito'),
    path('solicitacao_transito/<int:pk>/editar/',           views.editar_solicitacao_transito,          name = 'editar_solicitacao_transito'),
    path('solicitacao_transito/nova/', 					    views.nova_solicitacao_transito,			name = 'nova_solicitacao_transito'),
    # Educação
    path('solicitacao_educacao/',						   views.lista_solicitacao_educacao,			name = 'lista_solicitacao_educacao'),
    path('solicitacao_educacao/<int:pk>/',				   views.detalhe_solicitacao_educacao,			name = 'detalhe_solicitacao_educacao'),
    path('solicitacao_educacao/<int:pk>/editar/',          views.editar_solicitacao_educacao,           name = 'editar_solicitacao_educacao'),
    path('solicitacao_educacao/nova/', 					   views.nova_solicitacao_educacao, 			name = 'nova_solicitacao_educacao'),
    # Iluminação
    path('solicitacao_iluminacao/',						   views.lista_solicitacao_iluminacao,			name = 'lista_solicitacao_iluminacao'),
    path('solicitacao_iluminacao/<int:pk>/',			   views.detalhe_solicitacao_iluminacao,		name = 'detalhe_solicitacao_iluminacao'),
    path('solicitacao_iluminacao/<int:pk>/editar/',        views.editar_solicitacao_iluminacao,         name = 'editar_solicitacao_iluminacao'),
    path('solicitacao_iluminacao/nova/', 				   views.nova_solicitacao_iluminacao, 			name = 'nova_solicitacao_iluminacao'),
    # UPA
    path('solicitacao_upa/',                               views.lista_solicitacao_upa,                 name = 'lista_solicitacao_upa'),
    path('solicitacao_upa/<int:pk>/',                      views.detalhe_solicitacao_upa,               name = 'detalhe_solicitacao_upa'),
    path('solicitacao_upa/<int:pk>/editar/',               views.editar_solicitacao_upa,                name = 'editar_solicitacao_upa'),
    path('solicitacao_upa/nova/',                          views.nova_solicitacao_upa,                  name = 'nova_solicitacao_upa'),
    # Rest Transito
    path('rest/solicitacao_transito/',                     views.rest_lista_solicitacao_transito,       name = 'rest_lista_solicitacao_transito'),
    path('rest/solicitacao_transito/<pk>/',                views.rest_detalhe_solicitacao_transito,     name = 'rest_detalhe_solicitacao_transito'),
    # Rest Educacao
    path('rest/solicitacao_educacao/',                     views.rest_lista_solicitacao_educacao,       name = 'rest_lista_solicitacao_educacao'),
    path('rest/solicitacao_educacao/<pk>/',                views.rest_detalhe_solicitacao_educacao,     name = 'rest_detalhe_solicitacao_educacao'),
    # Rest Iluminação
    path('rest/solicitacao_iluminacao/',                   views.rest_lista_solicitacao_iluminacao,     name = 'rest_lista_solicitacao_iluminacao'),
    path('rest/solicitacao_iluminacao/<pk>/',              views.rest_detalhe_solicitacao_iluminacao,   name = 'rest_detalhe_solicitacao_iluminacao'),
    # Rest UPA
    path('rest/solicitacao_upa/',                          views.rest_lista_solicitacao_upa,            name = 'rest_lista_solicitacao_upa'),
    path('rest/solicitacao_upa/<pk>/',                     views.rest_detalhe_solicitacao_upa,          name = 'rest_detalhe_solicitacao_upa'),
    # Rest User
    path('rest/signup/', 								   views.registration_user, 				    name = 'registration_user'),
]