from django.db import models

from .middleware import current_tenant


class TenantAwareManager(models.Manager):
    def get_queryset(self):
        tenant = current_tenant()

        # If the manager was built from a queryset using
        # SomeQuerySet.as_manager() or SomeManager.from_queryset(),
        # we want to use that queryset instead of TenantAwareQuerySet.
        if self._queryset_class != models.QuerySet:
            return super().get_queryset().filter(tenant=tenant)

        return TenantAwareQuerySet(self.model, using=self._db).filter(
            tenant=tenant
        )


class TenantAwareQuerySet(models.QuerySet):
    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
        objs = list(objs)
        for o in objs:
            o.tenant = current_tenant()

        super().bulk_create(objs, batch_size, ignore_conflicts)

    def as_manager(cls):
        manager = TenantAwareManager.from_queryset(cls)()
        manager._built_with_as_manager = True
        return manager

    as_manager.queryset_only = True

    as_manager = classmethod(as_manager)
