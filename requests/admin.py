from django.contrib import admin
from .models import SolicitacaoTransito, SolicitacaoEducacao, SolicitacaoIluminacao, SolicitacaoMeioAmbiente

admin.site.register(SolicitacaoTransito)
admin.site.register(SolicitacaoEducacao)
admin.site.register(SolicitacaoIluminacao)
admin.site.register(SolicitacaoMeioAmbiente)
