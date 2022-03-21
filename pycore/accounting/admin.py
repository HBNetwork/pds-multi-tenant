from django.contrib import admin

from accounting.models import Invoice, Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    fields = ["cnpj", "corporate_name"]

admin.site.register(Invoice)
