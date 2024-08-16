from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from account.models import PointDeVente
from account.serializer import PointDeVente

class SponsorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta():
        model = Sponsor
        fields = ["image", "pk"]
    
    def get_image(self, obj):
        request = self.context.get('request')
        if request is not None:
            base_uri = f"{request.scheme}://{request.get_host()}"
            return f"{base_uri}{obj.image.url}"
        return obj.image.url
    
class EventSerealiser(serializers.ModelSerializer):
    nom = serializers.CharField()
    lieu = serializers.CharField()
    date = models.DateField(null=True, default=None)
    H_debut = models.TimeField(null=True, default=None)
    H_fin = models.TimeField(null=True, default=None)
    slug = serializers.SlugField(read_only = True)
    type_event = serializers.ChoiceField([
            ('Festival', 'Festival'),
            ('Soiré', 'Soiré'),
            ("Salon & Foire", "Salon & Foire"),
            ("Concert", "Concert")
        ],
        allow_blank = True
    )
    sponsors_images = serializers.SerializerMethodField()
    image = serializers.ImageField()
    organisateur = serializers.SerializerMethodField(read_only = True)

    class Meta():
        model = Evenement
        fields = ["nom", 'lieu', 'slug', "image", "H_debut", "H_fin", 'date', 'organisateur', 'sponsors_images', 'type_event']

    def get_organisateur(self, obj):
        organisteur = obj.owner
        return {'id' : organisteur.id, 'name' : organisteur.username}
    
    def get_sponsors_images(self, obj):
        request = self.context.get('request')
        event = obj
        sponsors = event.related_sponsors.all()
        sponsorSerial = SponsorSerializer(sponsors, many=True, context={'request': request}).data
        return sponsorSerial

class TicketSerealiser(serializers.ModelSerializer):
    type_ticket = serializers.CharField()
    nb_ticket = serializers.IntegerField()
    event = serializers.SerializerMethodField(read_only = True)
    prix = serializers.DecimalField(max_digits=10, decimal_places=0)
    
    class Meta():
        model = Ticket
        fields = ['type_ticket', 'nb_ticket', 'event', 'pk', "prix"]
        
    def get_event(self, obj):
        event = obj.event
        print(EventSerealiser(event).data)
        if event:
            return {'id': event.id, 'nom': event.nom} 
        else:
            return None

class AddTicketSerializer(serializers.ModelSerializer):
    type_ticket = serializers.CharField()
    nb_ticket = serializers.IntegerField()
    event = serializers.SerializerMethodField(read_only = True)
    prix = serializers.DecimalField(max_digits=10, decimal_places=0)

    class Meta():
        model = AddTicket
        fields = ['type_ticket', 'nb_ticket', 'event', 'pk', 'prix']
        
    def get_event(self, obj):
        event = obj.event
        print(EventSerealiser(event).data)
        if event:
            return {'id': event.id, 'nom': event.nom} 
        else:
            return None
        
class TicketQrCodeSerialiser(serializers.ModelSerializer):
    qr_image = serializers.ImageField()#Donné type, num, event
    num = serializers.DecimalField(max_digits = 6, decimal_places=0)    
    type_ticket = serializers.CharField()
    is_disabled = serializers.BooleanField()
    event = serializers.SerializerMethodField(read_only = True)
    addOwner = serializers.SerializerMethodField(read_only = True)
    
    class Meta():
        model = TicketQrCode
        fields = ['qr_image' , 'event', 'addOwner', 'type_ticket', 'is_disabled', 'num']
    
    def get_event(self, obj):
        event = obj.event
        eventSerialiser = EventSerealiser(event).data
        return eventSerialiser
    
    def get_addOwner(self, obj):
        return None