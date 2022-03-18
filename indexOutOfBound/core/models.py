from django.db import models

# Create your models here.


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    database_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
