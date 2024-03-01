from django.conf import settings
from django.shortcuts import render
from .models import *
from .serializer import *
import requests
from rest_framework import generics
from requests import Response
# Create your views here.


class LoginPDV(generics.ListCreateAPIView):
    queryset = PointDeVente.objects.all()
    serializer_class = PointDeVenteSerializer

class GoogleLoginRedirectView(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        client_secret = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
        try:
            code = request.data.get('code')
            print("code", code)
            token_endpoint = 'https://oauth2.googleapis.com/token'
            token_params = {
            "code" : code,  
            "client_id":client_id,
            "client_secret":client_secret,
            "redirect_uri":"http://localhost:5173/point-de-vente/",
            "grant_type":"authorization_code"
            } 
            response = requests.post(token_endpoint, token_params)
            print("responseBack", response.json())
            return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({"error": "Erreur de connexion", "details": str(e)}, status=500)
        
