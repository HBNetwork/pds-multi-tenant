from django.db.models import Sum
from django.shortcuts import render

from .models import Operacao
from .middleware import current_tenant


def index(request):
    context = {
        'tenant': current_tenant(),
    }
    return render(request, 'core/index.html', context=context)


def saldo(request):
    operacao = Operacao.objects.aggregate(saldo=Sum('valor', default=0))
    context = {
        'saldo': operacao['saldo'],
    }
    return render(request, 'core/saldo.html', context=context)
