from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from account.models import PointDeVente
from account.serializer import PointDeVente

class SponsorSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    
    class Meta():
        model = Sponsor
        fields = ["image"]
    
    
class EventSerealiser(serializers.ModelSerializer):
    nom = serializers.CharField()
    lieu = serializers.CharField()
    slug = serializers.SlugField(read_only = True)
    sponsors_images = serializers.SerializerMethodField()
    image = serializers.ImageField()
    organisateur = serializers.SerializerMethodField(read_only = True)

    class Meta():
        model = Evenement
        fields = ["nom", 'lieu', 'slug', "image", 'organisateur', 'sponsors_images']

    def get_organisateur(self, obj):
        organisteur = obj.owner
        return {'id' : organisteur.id, 'name' : organisteur.username}
    
    def get_sponsors_images(self, obj):
        event = obj
        sponsors = event.related_sponsors.all()
        sponsorSerial = SponsorSerializer(sponsors, many = True).data
        return sponsorSerial

class TicketSerealiser(serializers.ModelSerializer):
    type_ticket = serializers.CharField()
    nb_ticket = serializers.IntegerField()
    event = serializers.SerializerMethodField(read_only = True)
    class Meta():
        model = Ticket
        fields = ['type_ticket', 'nb_ticket', 'event']
        
    def get_event(self, obj):
        event = obj.event
        print(EventSerealiser(event).data)
        if event:
            return {'id': event.id, 'nom': event.nom} 
        else:
            return None
        