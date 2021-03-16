from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ReceberEmail
import sys
import imaplib
import email
from django.utils import timezone
from email import policy



@login_required
def lista_resposta(request):
    M = imaplib.IMAP4_SSL('imap.gmail.com')
    user = 'solicidadao@gmail.com'
    password = 'mwaowmhporretuug'

    try:
        M.login(user, password)

    except imaplib.IMAP4.error:
        print("erro")

    def process_mailbox(M):
        rv, data = M.search(None, "ALL")
        if rv != 'OK':
            print ("No messages found!")
            return

        for num in data[0].split():
            rv, data = M.fetch(num, '(RFC822)')
            if rv != 'OK':
                print ("ERROR getting message", num)
                return
            msg = email.message_from_bytes(data[0][1], policy=policy.SMTPUTF8)
            assunto = msg['Subject']
            body = msg.get_body(('plain',))
            if body:
                body = body.get_content()
            separandoTexto = body.split("Email do Solicitante:")
            emailUser = separandoTexto[1].split(">")
            mail = emailUser[0].split("\n")
            spaceEmail = mail[0]
            clienteEmail = spaceEmail.strip()
            separandoResposta = body.split("Em")
            respostasemEspaco = separandoResposta[0].split("\r")
            resposta = respostasemEspaco[0]
            convertDate = msg['Date']
            data = convertDate.split(',')
            hora = data[1].split('-')
            convertido = hora[0]
            usuario = request.user
            if (clienteEmail == usuario.email):
                if not ReceberEmail.objects.filter(email_id = request.user.id, assunto = assunto, data_resposta = convertido).exists():
                    getEmail = ReceberEmail.objects.create(email = request.user, assunto = assunto, resposta = resposta, data_resposta = convertido)

    rv, data = M.select("Inbox")
    if rv == 'OK':
        process_mailbox(M)
        M.close()
    M.logout()   
    respostas = ReceberEmail.objects.filter(email_id = request.user.id)
    return render(request, 'solicidadao/resposta/lista_resposta.html', {'respostas': respostas})


@login_required
def detalhe_resposta(request, pk):
    resposta = get_object_or_404(ReceberEmail, pk=pk)
    return render(request, 'solicidadao/resposta/detalhe_resposta.html', {'resposta': resposta})
 