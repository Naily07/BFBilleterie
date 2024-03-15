from django.contrib import admin
from .models import *
# Register your models here.

class PointDeVenteAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "owner")

class GlobalAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "account_type")

admin.site.register(PointDeVente, PointDeVenteAdmin)
admin.site.register(CustomUser, GlobalAdmin)
