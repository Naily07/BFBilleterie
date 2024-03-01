from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

class PointDeVenteSerializer(serializers.Serializer):
    lieu = serializers.CharField()
    contact = serializers.CharField()
    
    class Meta():
        models = PointDeVente
        fields = ["contact", "lieu"]