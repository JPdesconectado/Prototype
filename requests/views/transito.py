from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from requests.serializers import TransitoSerializer
from requests.models import SolicitacaoTransito, Endereco
from requests.forms import FormularioSolicitacaoTransito
import logging
logger = logging.getLogger(__name__)

def inicio(request):
    return render(request, 'solicidadao/inicio.html')

@login_required
def lista_solicitacao_transito(request):
    solicitacoes_transito = SolicitacaoTransito.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/transito/lista_solicitacao_transito.html', {'solicitacoes_transito' : solicitacoes_transito})

@login_required
def detalhe_solicitacao_transito(request, pk):
    solicitacao_transito = get_object_or_404(SolicitacaoTransito, pk=pk)
    return render(request, 'solicidadao/transito/detalhe_solicitacao_transito.html', {'solicitacao_transito': solicitacao_transito})

@login_required
def nova_solicitacao_transito(request):
    if request.method == "POST":
        form = FormularioSolicitacaoTransito(request.POST, request.FILES)
        if form.is_valid():
            solicitacao_transito = form.save(commit = False)
            solicitacao_transito.nome = request.user
            endereco = Endereco.objects.create(bairro = form.cleaned_data['bairro'], rua = form.cleaned_data['rua'], numero = form.cleaned_data['numero'], complemento = form.cleaned_data['complemento'])
            endereco.save()
            solicitacao_transito.endereco = endereco
            if ".pdf" in solicitacao_transito.imagem.name:
                logging.error("Formato não aceito. (.pdf)")
                messages.error(request, "Por favor, use o formato PNG ou JPG.")
                return redirect("nova_solicitacao_transito")
            solicitacao_transito.save()
            messages.success(request, 'Solicitação Enviada com Sucesso!')
            return redirect('detalhe_solicitacao_transito', pk = solicitacao_transito.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros abaixo.')    
    else:
        form = FormularioSolicitacaoTransito()
    return render(request, 'solicidadao/transito/editar_solicitacao_transito.html', {'form' : form})  

@login_required
def editar_solicitacao_transito(request, pk):
    solicitacao_transito = get_object_or_404(SolicitacaoTransito, pk=pk)
    if request.method == "POST":
        form = FormularioSolicitacaoTransito(request.POST, request.FILES, instance=solicitacao_transito)
        if form.is_valid():
            solicitacao_transito = form.save(commit = False)
            solicitacao_transito.nome = request.user
            endereco = Endereco.objects.create(bairro = form.cleaned_data['bairro'], rua = form.cleaned_data['rua'], numero = form.cleaned_data['numero'], complemento = form.cleaned_data['complemento'])
            endereco.save()
            solicitacao_transito.endereco = endereco
            if ".pdf" in solicitacao_transito.imagem.name:
                logging.error("Formato não aceito. (.pdf)")
                messages.error(request, "Por favor, use o formato PNG ou JPG.")
                return redirect("nova_solicitacao_transito")
            solicitacao_transito.save()
            messages.success(request, 'Solicitação Enviada com Sucesso!')
            return redirect('detalhe_solicitacao_transito', pk = solicitacao_transito.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros abaixo.')    
    else:
        form = FormularioSolicitacaoTransito()
    return render(request, 'solicidadao/transito/editar_solicitacao_transito.html', {'form' : form}) 

@api_view(['GET', 'POST'])
def rest_lista_solicitacao_transito(request):
    if request.method == 'GET':
        solicitacao_transito = SolicitacaoTransito.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
        serializer = TransitoSerializer(solicitacao_transito, many=True)   
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TransitoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)      

@api_view(['GET', 'PUT', 'DELETE'])
def rest_detalhe_solicitacao_transito(request, pk):
    try:
        solicitacao_transito = SolicitacaoTransito.objects.get(pk=pk)
    except SolicitacaoTransito.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransitoSerializer(solicitacao_transito)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TransitoSerializer(solicitacao_transito, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)             
    elif request.method == 'DELETE':
        solicitacao_transito.delete()
        return Response(status=status.HTTP_200_OK)