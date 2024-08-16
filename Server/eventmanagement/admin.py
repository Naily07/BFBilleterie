from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Sponsor)
# admin.site.register(PointDeVenteToEvenement)

class AddTicketAdmin(admin.ModelAdmin):
    list_display = ('type_ticket', 'pk' )

class PointDeVenteToEventAdmin(admin.ModelAdmin):
    list_display = ['pk']

class EventAdmin(admin.ModelAdmin):
    list_display = ['pk', 'nom']

admin.site.register(Evenement, EventAdmin)
admin.site.register(AddTicket, AddTicketAdmin)
admin.site.register(Ticket, AddTicketAdmin)
admin.site.register(TicketQrCode)
admin.site.register(PointDeVenteToEvenement, PointDeVenteToEventAdmin)