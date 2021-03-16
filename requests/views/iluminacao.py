from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from requests.serializers import IluminacaoSerializer
from requests.models import SolicitacaoIluminacao
from requests.forms import FormularioSolicitacaoIluminacao
import logging

logger = logging.getLogger(__name__)

@login_required
def lista_solicitacao_iluminacao(request):
    if request.user.is_superuser:
        solicitacoes_iluminacao = SolicitacaoIluminacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    else:
        solicitacoes_iluminacao = SolicitacaoIluminacao.objects.filter(email_id  = request.user.id, data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/iluminacao/lista_solicitacao_iluminacao.html', {'solicitacoes_iluminacao': solicitacoes_iluminacao})
    
@login_required
def detalhe_solicitacao_iluminacao(request, pk):
    solicitacao_iluminacao = get_object_or_404(SolicitacaoIluminacao, pk=pk)
    return render(request, 'solicidadao/iluminacao/detalhe_solicitacao_iluminacao.html', {'solicitacao_iluminacao': solicitacao_iluminacao})

@login_required
def nova_solicitacao_iluminacao(request):
    if request.method == "POST":
        form = FormularioSolicitacaoIluminacao(request.POST, request.FILES)
        if form.is_valid():
            solicitacao_iluminacao = form.save(commit = False)
            solicitacao_iluminacao.email = request.user
            if ".pdf" not in solicitacao_iluminacao.conta_luz.name:
                logging.error("Formato não aceito. (.png)")
                messages.error(request, "Por favor, use o formato PDF.")
                return redirect("nova_solicitacao_iluminacao")
            solicitacao_iluminacao.save()
            messages.success(request, 'Solicitação Criada com Sucesso!')
            return redirect('detalhe_solicitacao_iluminacao', pk = solicitacao_iluminacao.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros abaixo.')    
    else:
        form = FormularioSolicitacaoIluminacao()
    return render(request, 'solicidadao/iluminacao/editar_solicitacao_iluminacao.html', {'form': form})

@login_required
def editar_solicitacao_iluminacao(request, pk):
    solicitacao_iluminacao = get_object_or_404(SolicitacaoIluminacao, pk=pk)
    if request.method == "POST":
        form = FormularioSolicitacaoIluminacao(request.POST, request.FILES, instance=solicitacao_iluminacao)
        if form.is_valid():
            solicitacao_iluminacao = form.save(commit = False)
            solicitacao_iluminacao.email = request.user
            if ".pdf" not in solicitacao_iluminacao.conta_luz.name:
                logging.error("Formato não aceito. (.png)")
                messages.error(request, "Por favor, use o formato PDF.")
                return redirect("nova_solicitacao_iluminacao")
            solicitacao_iluminacao.save()
            messages.success(request, 'Solicitação Editada com Sucesso!')
            return redirect('detalhe_solicitacao_iluminacao', pk = solicitacao_iluminacao.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros abaixo.')    
    else:
        form = FormularioSolicitacaoIluminacao()
    return render(request, 'solicidadao/iluminacao/editar_solicitacao_iluminacao.html', {'form': form})

@api_view(['GET', 'POST'])
def rest_lista_solicitacao_iluminacao(request):
    if request.method == 'GET':
        solicitacao_iluminacao = SolicitacaoIluminacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
        serializer = IluminacaoSerializer(solicitacao_iluminacao, many=True)   
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IluminacaoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)      

@api_view(['GET', 'PUT', 'DELETE'])
def rest_detalhe_solicitacao_iluminacao(request, pk):
    try:
        solicitacao_iluminacao = SolicitacaoIluminacao.objects.get(pk=pk)
    except SolicitacaoIluminacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IluminacaoSerializer(solicitacao_iluminacao)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IluminacaoSerializer(solicitacao_iluminacao, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)             
    elif request.method == 'DELETE':
        solicitacao_iluminacao.delete()
        return Response(status=status.HTTP_200_OK)