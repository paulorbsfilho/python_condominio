# Create your views here.

from django.shortcuts import get_object_or_404, render
from .forms import *
from .models import Apartamento, Proprietario


def index(request):
    list_of_aps= Apartamento.objects.order_by('numero')[:]
    context = {'list_of_aps': list_of_aps}
    return render(request, 'core/index.html', context)


def detail(request, pk):
    ap = get_object_or_404(Apartamento, pk=pk)
    return render(request, 'core/detail.html', {'ap': ap})


def cadastro(request):
    if request.method == 'POST':
        p = Proprietario()
        p.nome = request.POST.get('nome','nome nao encontrado')
        p.telefone = request.POST.get('telefone', 'telefone nao encontrado')
        p.save()
    return render(request, 'core/cadastro.html', {})


def tipodespesa(request):
    form = TipoDespesaForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
    return render(request, 'core/tipo_despesa.html', {'form': form})
