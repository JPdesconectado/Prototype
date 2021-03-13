from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from requests.serializers import MeioAmbienteSerializer
from requests.models import SolicitacaoMeioAmbiente, Endereco
from requests.forms import FormularioSolicitacaoMeioAmbiente
import logging

logger = logging.getLogger(__name__)

@login_required
def lista_solicitacao_meioambiente(request):
    solicitacoes_meioambiente = SolicitacaoMeioAmbiente.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/meioambiente/lista_solicitacao_meioambiente.html', {'solicitacoes_meioambiente': solicitacoes_meioambiente})

@login_required
def detalhe_solicitacao_meioambiente(request, pk):
    solicitacao_meioambiente = get_object_or_404(SolicitacaoMeioAmbiente, pk=pk)
    return render(request, 'solicidadao/meioambiente/detalhe_solicitacao_meioambiente.html', {'solicitacao_meioambiente': solicitacao_meioambiente})

@login_required
def nova_solicitacao_meioambiente(request):
    if request.method == "POST":
        form = FormularioSolicitacaoMeioAmbiente(request.POST)
        if form.is_valid():
            solicitacao_meioambiente = form.save(commit = False)
            solicitacao_meioambiente.nome = request.user
            endereco = Endereco.objects.create(bairro = form.cleaned_data['bairro'], rua = form.cleaned_data['rua'], numero = form.cleaned_data['numero'], complemento = form.cleaned_data['complemento'])
            endereco.save()
            solicitacao_meioambiente.endereco = endereco
            solicitacao_meioambiente.save()
            messages.success(request, 'Solicitação Enviada com Sucesso!')
            return redirect('detalhe_solicitacao_meioambiente', pk = solicitacao_meioambiente.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros abaixo.')        
    else:
        form = FormularioSolicitacaoMeioAmbiente()
    return render(request, 'solicidadao/meioambiente/editar_solicitacao_meioambiente.html', {'form': form})    

@login_required
def editar_solicitacao_meioambiente(request, pk):    
    solicitacao_meioambiente = get_object_or_404(SolicitacaoMeioAmbiente, pk=pk)
    if request.method == "POST":
        form = FormularioSolicitacaoMeioAmbiente(request.POST, instance=solicitacao_meioambiente)
        if form.is_valid():
            solicitacao_meioambiente = form.save(commit = False)
            solicitacao_meioambiente.nome = request.user
            endereco = Endereco.objects.create(bairro = form.cleaned_data['bairro'], rua = form.cleaned_data['rua'], numero = form.cleaned_data['numero'], complemento = form.cleaned_data['complemento'])
            endereco.save()
            solicitacao_meioambiente.endereco = endereco
            solicitacao_meioambiente.save()
            messages.success(request, 'Solicitação Enviada com Sucesso!')
            return redirect('detalhe_solicitacao_meioambiente', pk = solicitacao_meioambiente.pk)
        else:
            logging.error("Erro no Formulário.")
            messages.warning(request, 'Por favor, corrija os erros acima.')        
    else:
        form = FormularioSolicitacaoMeioAmbiente()
    return render(request, 'solicidadao/meioambiente/editar_solicitacao_meioambiente.html', {'form': form}) 

@api_view(['GET', 'POST'])
def rest_lista_solicitacao_meioambiente(request):
    if request.method == 'GET':
        solicitacao_meioambiente = SolicitacaoMeioAmbiente.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
        serializer = MeioAmbienteSerializer(solicitacao_meioambiente, many=True)   
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MeioAmbienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)      

@api_view(['GET', 'PUT', 'DELETE'])
def rest_detalhe_solicitacao_meioambiente(request, pk):
    try:
        solicitacao_meioambiente = SolicitacaoMeioAmbiente.objects.get(pk=pk)
    except Solicitacaomeioambiente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MeioAmbienteSerializer(solicitacao_meioambiente)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MeioAmbienteSerializer(solicitacao_meioambiente, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)             
    elif request.method == 'DELETE':
        solicitacao_meioambiente.delete()
        return Response(status=status.HTTP_200_OK)