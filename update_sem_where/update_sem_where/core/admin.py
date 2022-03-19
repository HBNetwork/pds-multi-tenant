from django.contrib import admin  # noqa
from django.contrib.auth.admin import UserAdmin

from update_sem_where.core.models import User

admin.site.register(User, UserAdmin)
