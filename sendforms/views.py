from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import EnviarEmailTransito, EnviarEmailEducacao, EnviarEmailIluminacao, EnviarEmailUPA
from django.core.mail import send_mail
from requests.models import SolicitacaoTransito, SolicitacaoEducacao, SolicitacaoIluminacao, SolicitacaoUPA
import logging

logger = logging.getLogger(__name__)

@login_required
def enviar_email_transito(request, pk):
    solicitacao_transito = get_object_or_404(SolicitacaoTransito, pk=pk)
    usuario = request.user
    enviaremail = EnviarEmailTransito.objects.create(email = usuario.email, tipo = solicitacao_transito.tipo, endereco = solicitacao_transito.endereco)
    if not enviaremail.endereco.complemento:
    	logger.info("Sem complemento.")

    if not str(solicitacao_transito.imagem):
    	logger.warning("Sem imagem do ocorrido.")
    send_mail(
        "Solicitacao " + enviaremail.tipo,
        "Nome: " + usuario.nome + "\n" +
        "Email do Solicitante: " + enviaremail.email + "\n" +
        "Endereço: Rua " + enviaremail.endereco.rua +
        ", n° " + str(enviaremail.endereco.numero) +
        ", " + enviaremail.endereco.bairro + 
        ", complemento: " + enviaremail.endereco.complemento + "\n" +
        "Descrição: " + solicitacao_transito.comentario + "\n" +
        "Imagem: " + "\n" +
        str(solicitacao_transito.imagem),
        'solicidadao@django.com',
        ['detracan@pmc.sc.gov.br'],
        fail_silently = False,
        )
    solicitacao_transito.delete()
    solicitacoes_transito = SolicitacaoTransito.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/transito/lista_solicitacao_transito.html', {'solicitacoes_transito' : solicitacoes_transito})
   
@login_required
def enviar_email_educacao(request, pk):
    solicitacao_educacao = get_object_or_404(SolicitacaoEducacao, pk=pk)
    usuario = request.user    
    enviaremail = EnviarEmailEducacao.objects.create(email = usuario.email, cadastro_pf = solicitacao_educacao.cadastro_pf, rg = solicitacao_educacao.rg)
    send_mail(
        "Solicitando Histórico Escolar",
        "Nome: " + usuario.nome + "\n" +
        "Email do Solicitante: " + enviaremail.email + "\n" 
        "RG: " + enviaremail.rg + "\n" +
        "CPF: " + enviaremail.cadastro_pf + "\n",
        'solicidadao@django.com',
        ['educacao@pmc.sc.gov.br'],
        fail_silently = False,
         )
    solicitacao_educacao.delete()
    solicitacoes_educacao = SolicitacaoEducacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/educacao/detalhe_solicitacao_educacao.html', {'solicitacoes_educacao': solicitacoes_educacao})

@login_required
def enviar_email_iluminacao(request, pk):
    solicitacao_iluminacao = get_object_or_404(SolicitacaoIluminacao, pk=pk)
    usuario = request.user
    enviaremail = EnviarEmailIluminacao.objects.create(email = usuario.email, rg = solicitacao_iluminacao.rg)    
    send_mail(
        "Solicitando Iluminação",
        "Nome: " + usuario.nome + "\n" +
        "Email do Solicitante: " + enviaremail.email + "\n" 
        "RG: " + enviaremail.rg + "\n" +
        "Conta de Luz: " + "\n" +
        str(solicitacao_iluminacao.conta_luz),
        'solicidadao@django.com',
        ['planejamento@pmc.sc.gov.br'],
        fail_silently = False,
         )
    solicitacao_iluminacao.delete()
    solicitacoes_iluminacao = SolicitacaoIluminacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/iluminacao/lista_solicitacao_iluminacao.html', {'solicitacoes_iluminacao': solicitacoes_iluminacao})

@login_required
def enviar_email_upa(request, pk):
    solicitacao_upa = get_object_or_404(SolicitacaoUPA, pk=pk)
    usuario = request.user
    enviaremail = EnviarEmailUPA.objects.create(email = usuario.email, rg = solicitacao_upa.rg, card_sus = solicitacao_upa.card_sus)    
    send_mail(
        "Solicitando Atendimento",
        "Nome: " + usuario.nome + "\n" +
        "Email do Solicitante: " + enviaremail.email + "\n" 
        "RG: " + enviaremail.rg + "\n" +
        "N° Cartão SUS: " + enviaremail.card_sus + "\n" +
        "Comprovante de Residência: " + "\n" +
        str(solicitacao_upa.comprovante_residencia),
        'solicidadao@django.com',
        ['saude@pmc.sc.gov.br'],
        fail_silently = False,
         )
    solicitacao_upa.delete()
    solicitacoes_upa = SolicitacaoUPA.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/upa/lista_solicitacao_upa.html', {'solicitacoes_upa': solicitacoes_upa})
