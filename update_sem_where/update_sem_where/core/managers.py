from django.db import connection, models


class SchemaManager(models.Manager):
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SET search_path to pg_catalog")
            return super().get_queryset()

    def tenants(self):
        schemas = self.exclude(
            name__iregex=r'(^pg_|information_schema|public)'
        )
        return [s.name for s in schemas]
