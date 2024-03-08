from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

class PointDeVenteSerializer(serializers.ModelSerializer):
    lieu = serializers.CharField()
    # tel =  serializers.CharField()
    email = serializers.EmailField()
    list_event = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField(read_only = True)
    is_active = serializers.BooleanField(read_only=True)
    class Meta():
        model = PointDeVente
        fields = ['lieu', "email", 'list_event', 'owner', "pk", "is_active"]

    def get_list_event(self, obj):
        from eventManagement.serializer import EventSerealiser
        from eventManagement.models import PointDeVenteToEvenement
        try:
            pdv_name = obj.id
            #Get point de vente to Event avec le point de vente actuelle
            relations = PointDeVenteToEvenement.objects.filter(pdv = pdv_name)
            #Get event attribuer a cet point de vente
            for relation in relations:
                print(relation)
            events = [relation.event for relation in relations]
            eventsSerializer = EventSerealiser(events, many = True).data
            return eventsSerializer
        except Exception as e:
            print("Execpt list", e)
            return None
        
    def get_owner(self, obj):
        request = self.context.get('request')
        # print(f"User créer {request.user} to pdv {obj.username}")
        user = request.user
        return {"username" : user.username, "id" : user.id}
    