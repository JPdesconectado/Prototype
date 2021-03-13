from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import EnviarEmailTransito, EnviarEmailEducacao, EnviarEmailIluminacao, EnviarEmailMeioAmbiente
from django.core.mail import send_mail, EmailMessage
from requests.models import SolicitacaoTransito, SolicitacaoEducacao, SolicitacaoIluminacao, SolicitacaoMeioAmbiente
import logging

logger = logging.getLogger(__name__)

@login_required
def enviar_email_transito(request, pk):
    solicitacao_transito = get_object_or_404(SolicitacaoTransito, pk=pk)
    usuario = request.user
    enviaremail = EnviarEmailTransito.objects.create(   
                                                    email = usuario.email, 
                                                    tipo = solicitacao_transito.tipo, 
                                                    endereco = solicitacao_transito.endereco, 
                                                    imagem = solicitacao_transito.imagem
                                                    )

    if not enviaremail.endereco.complemento:
    	logger.info("Sem complemento.")

    if not str(solicitacao_transito.imagem):
    	logger.warning("Sem imagem do ocorrido.")

    email = EmailMessage(
    		"Solicitacao " + enviaremail.tipo, #título

    		"Nome: " + usuario.nome + "\n" +	#corpo do email (
        	"Email do Solicitante: " + enviaremail.email + "\n" +
        	"Endereço: Rua " + enviaremail.endereco.rua +
        	", n° " + str(enviaremail.endereco.numero) +
        	", " + enviaremail.endereco.bairro + 
        	", complemento: " + enviaremail.endereco.complemento + "\n" +
        	"Descrição: " + solicitacao_transito.comentario + "\n" +
        	"Imagem: " + "\n", # ) fim do corpo do email

        	'solicidadao@gmail.com', # emissor

        	['jhony.pv@aluno.ifsc.edu.br'] # receptor
    	)

    email.attach_file('media/' +  str(solicitacao_transito.imagem)) # anexando imagem
    email.send() # enviando

    solicitacao_transito.delete()
    solicitacoes_transito = SolicitacaoTransito.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/transito/lista_solicitacao_transito.html', {'solicitacoes_transito' : solicitacoes_transito})
   
@login_required
def enviar_email_educacao(request, pk):
    solicitacao_educacao = get_object_or_404(SolicitacaoEducacao, pk=pk)
    usuario = request.user    
    enviaremail = EnviarEmailEducacao.objects.create(
                                                    email = usuario.email, 
                                                    cadastro_pf = solicitacao_educacao.cadastro_pf, 
                                                    rg = solicitacao_educacao.rg
                                                    )

    email = EmailMessage(
        "Solicitando Histórico Escolar",

        "Nome: " + usuario.nome + "\n" +
        "Email do Solicitante: " + enviaremail.email + "\n" 
        "RG: " + enviaremail.rg + "\n" +
        "CPF: " + enviaremail.cadastro_pf + "\n",

        'solicidadao@gmail.com',
        ['jhony.pv@aluno.ifsc.edu.br'],
        )
    email.send()
    solicitacao_educacao.delete()
    solicitacoes_educacao = SolicitacaoEducacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/educacao/lista_solicitacao_educacao.html', {'solicitacoes_educacao': solicitacoes_educacao})

@login_required
def enviar_email_iluminacao(request, pk):
    solicitacao_iluminacao = get_object_or_404(SolicitacaoIluminacao, pk=pk)
    usuario = request.user
    enviaremail = EnviarEmailIluminacao.objects.create ( 
                                                       email = usuario.email, 
                                                       rg = solicitacao_iluminacao.rg, 
                                                       conta_luz = solicitacao_iluminacao.conta_luz
                                                       )    
    email = EmailMessage(
        "Solicitando Iluminação",

        "Nome: " + usuario.nome + "\n" +
        "Email do Solicitante: " + enviaremail.email + "\n" 
        "RG: " + enviaremail.rg + "\n" +
        "Conta de Luz: " + "\n",

        'solicidadao@gmail.com',

        ['jhony.pv@aluno.ifsc.edu.br'],
         )

    email.attach_file('media/' +  str(solicitacao_iluminacao.conta_luz))
    email.send()     

    solicitacao_iluminacao.delete()
    solicitacoes_iluminacao = SolicitacaoIluminacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/iluminacao/lista_solicitacao_iluminacao.html', {'solicitacoes_iluminacao': solicitacoes_iluminacao})

@login_required
def enviar_email_meioambiente(request, pk):
    solicitacao_meioambiente = get_object_or_404(SolicitacaoMeioAmbiente, pk=pk)
    usuario = request.user
    enviaremail = EnviarEmailMeioAmbiente.objects.create(email = usuario.email, endereco = solicitacao_meioambiente.endereco) 
    if not enviaremail.endereco.complemento:
        logger.info("Sem complemento.")   
    email = EmailMessage(
    		"Solicitando Remoção de Resíduos Vegetais",
    		
            "Nome: " + usuario.nome + "\n" +    #corpo do email (
            "Email do Solicitante: " + enviaremail.email + "\n" +
            "Endereço: Rua " + enviaremail.endereco.rua +
            ", n° " + str(enviaremail.endereco.numero) +
            ", " + enviaremail.endereco.bairro + 
            ", complemento: " + enviaremail.endereco.complemento + "\n",

            'solicidadao@gmail.com', # emissor

            ['jhony.pv@aluno.ifsc.edu.br'] # receptor
        )

    email.send() 
    solicitacao_meioambiente.delete()
    solicitacoes_meioambiente = SolicitacaoMeioAmbiente.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/meioambiente/lista_solicitacao_meioambiente.html', {'solicitacoes_meioambiente': solicitacoes_meioambiente})
