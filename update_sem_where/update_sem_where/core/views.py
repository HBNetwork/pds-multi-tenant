from django.shortcuts import render

from update_sem_where.core import tenants


def index(request):
    return render(request, 'index.html', {'tenants': tenants.list()})
