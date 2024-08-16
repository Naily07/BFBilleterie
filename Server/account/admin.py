from django.contrib import admin
from .models import *
# Register your models here.

class PointDeVenteAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "email", "owner", 'sub')

class GlobalAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "email", "account_type", 'sub')

admin.site.register(PointDeVente, PointDeVenteAdmin)
admin.site.register(CustomUser, GlobalAdmin)
