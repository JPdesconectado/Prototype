from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from requests.serializers import UPASerializer
from requests.models import SolicitacaoUPA
from requests.forms import FormularioSolicitacaoUPA
import logging

logger = logging.getLogger(__name__)

@login_required
def lista_solicitacao_upa(request):
    solicitacoes_upa = SolicitacaoUPA.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/upa/lista_solicitacao_upa.html', {'solicitacoes_upa': solicitacoes_upa})

@login_required
def detalhe_solicitacao_upa(request, pk):
    solicitacao_upa = get_object_or_404(SolicitacaoUPA, pk=pk)
    return render(request, 'solicidadao/upa/detalhe_solicitacao_upa.html', {'solicitacao_upa': solicitacao_upa})

@login_required
def nova_solicitacao_upa(request):
    if request.method == "POST":
        form = FormularioSolicitacaoUPA(request.POST, request.FILES)
        if form.is_valid():
            solicitacao_upa = form.save(commit = False)
            solicitacao_upa.nome = request.user
            if ".pdf" not in solicitacao_upa.comprovante_residencia.name:
                logging.error("Formato não aceito.")
                messages.error(request, "Por favor, use o formato PDF.")
                return redirect("nova_solicitacao_upa")
            solicitacao_upa.save()
            messages.success(request, 'Solicitação Enviada com Sucesso!')
            return redirect('detalhe_solicitacao_upa', pk = solicitacao_upa.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros abaixo.')        
    else:
        form = FormularioSolicitacaoUPA()
    return render(request, 'solicidadao/upa/editar_solicitacao_upa.html', {'form': form})    

@login_required
def editar_solicitacao_upa(request, pk):    
    solicitacao_upa = get_object_or_404(SolicitacaoUPA, pk=pk)
    if request.method == "POST":
        form = FormularioSolicitacaoUPA(request.POST, instance=solicitacao_upa)
        if form.is_valid():
            solicitacao_upa = form.save(commit = False)
            solicitacao_upa.nome = request.user
            if ".pdf" not in solicitacao_upa.comprovante_residencia.name:
                logging.error("Formato não aceito.")
                messages.error(request, "Por favor, use o formato PDF.")
                return redirect("nova_solicitacao_upa")
            solicitacao_upa.save()
            messages.success(request, 'Solicitação Enviada com Sucesso!')
            return redirect('detalhe_solicitacao_upa', pk = solicitacao_upa.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros acima.')        
    else:
        form = FormularioSolicitacaoUPA()
    return render(request, 'solicidadao/upa/editar_solicitacao_upa.html', {'form': form}) 

@api_view(['GET', 'POST'])
def rest_lista_solicitacao_upa(request):
    if request.method == 'GET':
        solicitacao_upa = SolicitacaoUPA.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
        serializer = UPASerializer(solicitacao_upa, many=True)   
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UPASerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)      

@api_view(['GET', 'PUT', 'DELETE'])
def rest_detalhe_solicitacao_upa(request, pk):
    try:
        solicitacao_upa = SolicitacaoUPA.objects.get(pk=pk)
    except SolicitacaoUPA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UPASerializer(solicitacao_upa)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UPASerializer(solicitacao_upa, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)             
    elif request.method == 'DELETE':
        solicitacao_upa.delete()
        return Response(status=status.HTTP_200_OK)