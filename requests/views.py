from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Solicitacao
from django.contrib.auth.decorators import login_required
from .forms import FormularioSolicitacao


def inicio(request):
    return render(request, 'detracan/inicio.html')

@login_required
def lista_solicitacao(request):
    solicitacoes = Solicitacao.objects.filter(data_criacao__lte = timezone.now()).order_by('data_criacao')
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
            solicitacao.save()
            return redirect('detalhe_solicitacao', pk = solicitacao.pk)
    else:
        form = FormularioSolicitacao()
    return render(request, 'detracan/editar_solicitacao.html', {'form' : form})  

