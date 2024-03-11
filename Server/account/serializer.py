from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

class PointDeVenteSerializer(serializers.ModelSerializer):
    lieu = serializers.CharField(allow_blank = True)
    # tel =  serializers.CharField()
    email = serializers.EmailField(allow_blank = True)
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
            pdv_id = obj.id
            #Get point de vente to Event avec le point de vente actuelle
            relations = PointDeVenteToEvenement.objects.filter(pdv = pdv_id)
            #Get event attribuer a cet point de vente
            for relation in relations:
                print("relation username-event : ", relation)
            events = [relation.event for relation in relations]
            eventsSerializer = EventSerealiser(events, many = True).data
            listEvent = []
            for event in eventsSerializer:
                listEvent.append({"nom" : event["nom"], "slug" : event["slug"]})
            return listEvent
        except Exception as e:
            print("Execpt list_event", e)
            return None
        
    def get_owner(self, obj):
        pdv = obj
        owner = pdv.owner
        # print(f"User créer {request.user} to pdv {obj.username}")
        # user = request.user
        return {"username" : owner.username, "id" : owner.id}
    
class UserSerialiser(serializers.ModelSerializer):
    tel = serializers.CharField(allow_blank = True)
    account_type = serializers.ChoiceField(
        [
            ("client", "client"),
            ("organisateur", "organisateur")
        ],
        allow_blank = True
    )
    
    class Meta():
        model = MyUser
        fields = [ "email", 'username', 'tel', "pk", "account_type"]
    