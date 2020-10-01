from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from requests.serializers import EducacaoSerializer
from requests.models import SolicitacaoEducacao
from requests.forms import FormularioSolicitacaoEducacao
import logging

logger = logging.getLogger(__name__)


@login_required
def lista_solicitacao_educacao(request):
    if request.user.is_superuser:
        solicitacoes_educacao = SolicitacaoEducacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    else:
        solicitacoes_educacao = SolicitacaoEducacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/educacao/lista_solicitacao_educacao.html', {'solicitacoes_educacao' : solicitacoes_educacao})

@login_required
def detalhe_solicitacao_educacao(request, pk):
    solicitacao_educacao = get_object_or_404(SolicitacaoEducacao, pk=pk)
    return render(request, 'solicidadao/educacao/detalhe_solicitacao_educacao.html', {'solicitacao_educacao': solicitacao_educacao})

@login_required
def nova_solicitacao_educacao(request):
    if request.method == "POST":
        form = FormularioSolicitacaoEducacao(request.POST)
        if form.is_valid():
            solicitacao_educacao = form.save(commit = False)
            solicitacao_educacao.nome = request.user
            solicitacao_educacao.save()
            messages.success(request, 'Solicitação Enviada com Sucesso!')
            return redirect('detalhe_solicitacao_educacao', pk = solicitacao_educacao.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros abaixo.')    
    else:
        form = FormularioSolicitacaoEducacao()
    return render(request, 'solicidadao/educacao/editar_solicitacao_educacao.html', {'form': form})            

@login_required
def editar_solicitacao_educacao(request, pk):
    solicitacao_educacao = get_object_or_404(SolicitacaoEducacao, pk=pk)
    if request.method == "POST":
        form = FormularioSolicitacaoEducacao(request.POST, instance=solicitacao_educacao)
        if form.is_valid():
            solicitacao_educacao = form.save(commit = False)
            solicitacao_educacao.nome = request.user
            solicitacao_educacao.save()
            messages.success(request, 'Solicitação Enviada com Sucesso!')
            return redirect('detalhe_solicitacao_educacao', pk = solicitacao_educacao.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros abaixo.')    
    else:
        form = FormularioSolicitacaoEducacao()
    return render(request, 'solicidadao/educacao/editar_solicitacao_educacao.html', {'form': form})   

@api_view(['GET', 'POST'])
def rest_lista_solicitacao_educacao(request):
    if request.method == 'GET':
        solicitacao_educacao = SolicitacaoEducacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
        serializer = EducacaoSerializer(solicitacao_educacao, many=True)   
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EducacaoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)      

@api_view(['GET', 'PUT', 'DELETE'])
def rest_detalhe_solicitacao_educacao(request, pk):
    try:
        solicitacao_educacao = SolicitacaoEducacao.objects.get(pk=pk)
    except SolicitacaoEducacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EducacaoSerializer(solicitacao_educacao)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EducacaoSerializer(solicitacao_educacao, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)             
    elif request.method == 'DELETE':
        solicitacao_educacao.delete()
        return Response(status=status.HTTP_200_OK)