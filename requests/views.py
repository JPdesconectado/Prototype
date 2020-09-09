from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Solicitacao, Status, Endereco
from django.contrib.auth.decorators import login_required
from .forms import FormularioSolicitacao, FormularioStatus


def inicio(request):
    return render(request, 'detracan/inicio.html')

@login_required
def lista_solicitacao(request):

    if request.user.is_superuser:
        solicitacoes = Solicitacao.objects.filter(data_criacao__lte = 
                                                  timezone.now()).order_by('data_criacao')
    else:    
        solicitacoes = Solicitacao.objects.filter(usuario = request.user.id, data_criacao__lte = 
                                                  timezone.now()).order_by('data_criacao')
    return render(request, 'detracan/lista_solicitacao.html', {'solicitacoes' : solicitacoes})

@login_required
def detalhe_solicitacao(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    return render(request, 'detracan/detalhe_solicitacao.html', {'solicitacao': solicitacao})

@login_required
def nova_solicitacao(request):
    if request.method == "POST":
        form = FormularioSolicitacao(request.POST, request.FILES)
        if form.is_valid():
            solicitacao = form.save(commit = False)
            solicitacao.usuario = request.user
            endereco = Endereco.objects.create(bairro = form.cleaned_data['bairro'], rua = form.cleaned_data['rua'], numero = form.cleaned_data['numero'], complemento = form.cleaned_data['complemento'])
            endereco.save()
            solicitacao.endereco = endereco
            status = Status.objects.create(atual = 'Recebido')
            status.save()
            solicitacao.save()
            return redirect('detalhe_solicitacao', pk = solicitacao.pk)
    else:
        form = FormularioSolicitacao()
    return render(request, 'detracan/editar_solicitacao.html', {'form' : form})  

@login_required
def editar_status(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if request.method == "POST":
        form = FormularioStatus(request.POST, instance=solicitacao)
        if form.is_valid():
            status = solicitacao.status
            status.atual = form.cleaned_data['atual']
            status.save()
            solicitacao.save()
            return redirect('detalhe_solicitacao', pk = solicitacao.pk)
            
    else:
        form = FormularioStatus(instance=solicitacao)

    return render(request, 'detracan/editar_status.html', {'form': form})