from django.shortcuts import render

from update_sem_where.core import tenants
from update_sem_where.core.thread import local


def index(request, **kwargs):
    return render(
        request,
        'index.html',
        {'tenants': tenants.list(), 'tenant': local.tenant},
    )
