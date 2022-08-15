from django.contrib import admin

from .models import Group, User, Gift

admin.site.register([Group, User, Gift])
