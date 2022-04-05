from django.db import models

# from .middleware import current_tenant_name, current_tenant
from .middleware import current_tenant_name


class TenantAwareManager(models.Manager):
    def get_queryset(self):
        # tenant_name = current_tenant_name()
        tenant_pk = current_tenant_name()

        # If the manager was built from a queryset using
        # SomeQuerySet.as_manager() or SomeManager.from_queryset(),
        # we want to use that queryset instead of TenantAwareQuerySet.
        if self._queryset_class != models.QuerySet:
            # return super().get_queryset().filter(tenant__name=tenant_name)
            return super().get_queryset().filter(tenant_id=tenant_pk)

        # return TenantAwareQuerySet(self.model, using=self._db).filter(
        #     tenant__slug=tenant_name
        # )
        return TenantAwareQuerySet(self.model, using=self._db).filter(
            tenant_id=tenant_pk
        )


class TenantAwareQuerySet(models.QuerySet):
    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
        objs = list(objs)
        for o in objs:
            # o.tenant = current_tenant()
            o.tenant_id = current_tenant_name()

        super().bulk_create(objs, batch_size, ignore_conflicts)

    def as_manager(cls):
        manager = TenantAwareManager.from_queryset(cls)()
        manager._built_with_as_manager = True
        return manager

    as_manager.queryset_only = True

    as_manager = classmethod(as_manager)
