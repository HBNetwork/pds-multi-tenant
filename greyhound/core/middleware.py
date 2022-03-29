import re

from django.conf import settings
from django.http import Http404


class NoTenant(Exception):
    ...


def split_tenant(path):
    if (match := re.search(r'/(.*?)(/.*)', path)):
        return match.groups()
    elif (match := re.search(r'/(.*)', path)):
        if (tenant := match.group(1)):
            return tenant, ''
    raise NoTenant(f'No tenant in {path}')


def tenant_available(tenant_name):
    return tenant_name in settings.TENANTS


def tenant_exempt(tenant_name):
    return tenant_name in settings.TENANTS_EXEMPT


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_name, path = self.get_tenant_from_url(request.path_info)

        if not tenant_exempt(tenant_name):
            self.check_tenant(tenant_name)
            request.tenant_name = tenant_name
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
        if not tenant_available(tenant_name):
            raise Http404()
