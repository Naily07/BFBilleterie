from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Evenement)
admin.site.register(Sponsor)
admin.site.register(PointDeVenteToEvenement)
admin.site.register(AddTicket)
admin.site.register(Ticket)
admin.site.register(TicketQrCode)