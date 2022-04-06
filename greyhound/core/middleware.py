import re
import threading

from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404

threadlocal = threading.local()


class NoTenant(Exception):
    ...


def split_tenant(path):
    if (match := re.search(r'/(.*?)(/.*)', path)):
        return match.groups()
    elif (match := re.search(r'/(.*)', path)):
        if (tenant := match.group(1)):
            return tenant, ''
    raise NoTenant(f'No tenant in {path}')


def tenant_exempt(tenant_name):
    if not hasattr(settings, 'TENANTS_EXEMPT'):
        return False
    return tenant_name in settings.TENANTS_EXEMPT


def current_tenant():
    try:
        return threadlocal.tenant
    except AttributeError as e:
        raise NoTenant('No tenant in thread')


def set_tenant(tenant):
    threadlocal.tenant = tenant


def reset_tenant():
    if not hasattr(threadlocal, 'tenant'):
        return
    delattr(threadlocal, 'tenant')


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # breakpoint()
        tenant_name, path = self.get_tenant_from_url(request.path_info)

        if not tenant_exempt(tenant_name):
            self.check_tenant(tenant_name)
            request.path_info = path

        return self.get_response(request)

    @staticmethod
    def get_tenant_from_url(path):
        try:
            return split_tenant(path)
        except NoTenant:
            raise Http404()

    @staticmethod
    def check_tenant(tenant_name):
        from .models import Tenant
        tenant = get_object_or_404(Tenant, slug=tenant_name)
        set_tenant(tenant)