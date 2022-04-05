import threading
from django.db.models import Sum
from django.shortcuts import render

from .models import Operacao

# threadlocal = threading.local()


def index(request):
    return render(request, 'core/index.html')


def saldo(request):
    operacao = Operacao.objects.aggregate(saldo=Sum('valor', default=0))
    context = {
        'saldo': operacao['saldo'],
    }
    return render(request, 'core/saldo.html', context=context)
