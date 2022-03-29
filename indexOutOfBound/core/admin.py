from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Tenant

admin.site.register(Tenant)


class TenantAdminSite(AdminSite):
    ...

tenant_admin_site = TenantAdminSite(name="Tenant Admin")
