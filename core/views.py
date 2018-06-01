# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response

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


def done(request):
    return render(request, 'core/done.html', {})