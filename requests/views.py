from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import SolicitacaoTransito, SolicitacaoEducacao, SolicitacaoIluminacao, SolicitacaoUPA, Status, Endereco
from django.contrib.auth.decorators import login_required
from .forms import FormularioSolicitacaoTransito, FormularioSolicitacaoEducacao, FormularioSolicitacaoIluminacao, FormularioSolicitacaoUPA, FormularioStatus


def inicio(request):
    return render(request, 'solicidadao/inicio.html')

@login_required
def lista_solicitacao_transito(request):
    if request.user.is_superuser:
        solicitacoes_transito = SolicitacaoTransito.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    else:    
        solicitacoes_transito = SolicitacaoTransito.objects.filter(nome_id = request.user.id, data_criacao__lte = timezone.now()).order_by('data_criacao')
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
            status = Status.objects.create(atual = 'Recebido')
            status.save()
            solicitacao_transito.save()
            return redirect('detalhe_solicitacao_transito', pk = solicitacao_transito.pk)
    else:
        form = FormularioSolicitacaoTransito()
    return render(request, 'solicidadao/transito/editar_solicitacao_transito.html', {'form' : form})  

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
            return redirect('detalhe_solicitacao_educacao', pk = solicitacao_educacao.pk)
    else:
        form = FormularioSolicitacaoEducacao()
    return render(request, 'solicidadao/educacao/editar_solicitacao_educacao.html', {'form': form})            

@login_required
def lista_solicitacao_iluminacao(request):
    solicitacoes_iluminacao = SolicitacaoIluminacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
    return render(request, 'solicidadao/iluminacao/lista_solicitacao_iluminacao.html', {'solicitacoes_iluminacao': solicitacoes_iluminacao})
    
@login_required
def detalhe_solicitacao_iluminacao(request, pk):
    solicitacao_iluminacao = get_object_or_404(SolicitacaoIluminacao, pk=pk)
    return render(request, 'solicidadao/iluminacao/detalhe_solicitacao_iluminacao.html', {'solicitacao_iluminacao': solicitacao_iluminacao})

def nova_solicitacao_iluminacao(request):
    if request.method == "POST":
        form = FormularioSolicitacaoIluminacao(request.POST, request.FILES)
        if form.is_valid():
            solicitacao_iluminacao = form.save(commit = False)
            solicitacao_iluminacao.nome = request.user
            solicitacao_iluminacao.save()
            return redirect('detalhe_solicitacao_iluminacao', pk = solicitacao_iluminacao.pk)
    else:
        form = FormularioSolicitacaoIluminacao()
    return render(request, 'solicidadao/iluminacao/editar_solicitacao_iluminacao.html', {'form': form})


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
        form = FormularioSolicitacaoUPA(request.POST)
        if form.is_valid():
            solicitacao_upa = form.save(commit = False)
            solicitacao_upa.nome = request.user
            solicitacao_upa.save()
            return redirect('detalhe_solicitacao_upa', pk = solicitacao_upa.pk)    
    else:
        form = FormularioSolicitacaoUPA()
    return render(request, 'solicidadao/upa/editar_solicitacao_upa.html', {'form': form})    

@login_required
def editar_status(request, pk):
    solicitacao = get_object_or_404(SolicitacaoTransito, pk=pk)
    if request.method == "POST":
        form = FormularioStatus(request.POST, instance=solicitacao)
        if form.is_valid():
            status = solicitacao.status
            status.atual = form.cleaned_data['atual']
            status.save()
            solicitacao.save()
            return redirect('detalhe_solicitacao_transito', pk = solicitacao.pk)
            
    else:
        form = FormularioStatus(instance = solicitacao)

    return render(request, 'solicidadao/editar_status.html', {'form': form})