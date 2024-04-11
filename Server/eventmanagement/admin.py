from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Evenement)
admin.site.register(Sponsor)
admin.site.register(PointDeVenteToEvenement)

class AddTicketAdmin(admin.ModelAdmin):
    list_display = ('type_ticket', 'pointdevente', )

admin.site.register(AddTicket, AddTicketAdmin)
admin.site.register(Ticket)
admin.site.register(TicketQrCode)