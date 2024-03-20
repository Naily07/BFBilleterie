from django.db import models
from django.contrib.auth.models import User

from account.models import CustomUser, PointDeVente
# Create your models here.

class Evenement(models.Model):
    nom = models.TextField(max_length = 255, unique = True)
    lieu = models.TextField(max_length = 25, default = None)
    image = models.ImageField(null = False, blank=False, upload_to="event/")
    slug = models.SlugField(unique=True, max_length=255)
    owner = models.ForeignKey(CustomUser, default = 1, on_delete=models.CASCADE, related_name = "evenement_related")
    
    def __str__(self):
        return self.nom
    
class PointDeVenteToEvenement(models.Model):
    pdv = models.ForeignKey(PointDeVente, on_delete=models.CASCADE, null = True)
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE, null = True, related_name = "PDVToEvent_related")

    def get_pdv(self, obj):
        pdv = obj.pdv
        return {"id" : pdv.id, "username" : pdv.name}

    def get_event(self, obj):
        event = obj.event
        return {"id" : event.id, "nom" : event.name}

    def __str__(self) -> str:
        return str(self.pdv ) + "-"+ str(self.event)
    

class Sponsor(models.Model):
    image = models.ImageField(default = None, upload_to="sponsors/")
    event = models.ForeignKey(Evenement, on_delete = models.CASCADE, default = None, related_name = 'related_sponsors')
    
    def image_url(self):
        # Renvoie le lien complet pour accéder à l'image
        return self.image.use_url

class TicketBase(models.Model):
    type_ticket = models.TextField(max_length = 24)
    nb_ticket  = models.IntegerField(default = 0, null = True)
    event = models.ForeignKey(Evenement, on_delete = models.SET_NULL, null = True, related_name = "%(class)s_related")#Addticket_related

    class Meta():
        abstract = True

class AddTicket(TicketBase):
    pointdevente = models.ForeignKey(PointDeVente, on_delete = models.CASCADE, null = True, related_name = "%(class)s_related")

    def __str__(self):
            return self.type_ticket

class Ticket(TicketBase):
    def __str__(self):
        return self.type_ticket

class ArchiveTicket(TicketBase):
    def __str__(self):
        return self.type_ticket    
    