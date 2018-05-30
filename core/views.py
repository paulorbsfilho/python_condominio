# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Apartamento, Proprietario


def index(request):
    list_of_aps= Apartamento.objects.order_by('numero')[:]
    context = {'list_of_aps': list_of_aps}
    return render(request, 'core/index.html', context)


def detail(request, pk):
    ap = get_object_or_404(Apartamento, pk=pk)
    return render(request, 'core/detail.html', {'ap': ap})
