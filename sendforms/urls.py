from django.urls import path
from . import views

urlpatterns = [
	path('solicitacao_transito/enviar/<int:pk>', views.enviar_email_transito, name = 'enviar_email_transito'),
	path('solicitacao_educacao/enviar/<int:pk>', views.enviar_email_educacao, name = 'enviar_email_educacao'),
	path('solicitacao_iluminacao/enviar/<int:pk>', views.enviar_email_iluminacao, name = 'enviar_email_iluminacao'),
	path('solicitacao_upa/enviar/<int:pk>', views.enviar_email_upa, name = 'enviar_email_upa'),
]