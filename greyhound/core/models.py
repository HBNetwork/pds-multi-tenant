from django.db import models

from .managers import TenantAwareManager


class Tenant(models.Model):
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class TenantAwareModelMixin(models.Model):
    tenant = models.ForeignKey("core.Tenant", models.CASCADE)

    objects = TenantAwareManager()
    unscoped = models.Manager()

    class Meta:
        abstract = True


class Operacao(TenantAwareModelMixin):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        verbose_name = 'operação'
        verbose_name_plural = 'operações'
