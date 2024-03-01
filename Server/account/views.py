from django.conf import settings
from django.shortcuts import render
from .models import *
from .serializer import *
import requests
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.


class LoginPDV(generics.ListCreateAPIView):
    queryset = PointDeVente.objects.all()
    serializer_class = PointDeVenteSerializer

    def create(self, request, *args, **kwargs):
        code = request.data.get('code')
        token = GoogleLoginGetToken(code)
        print('POSNTNTN', token)
        items = token.items()
        access_token = ""
        error = ""
        for key, value in items:
            if key == "access_token":
                access_token = value
            if key == "error":
                error = value
        print("Acces", access_token)
        if access_token:
            return Response({"token":access_token}, status=200)    
        elif error :
            return Response({"Error" : error})
    # def create(self, request, *args, **kwargs):

def GoogleLoginGetToken(code):
    client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    client_secret = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
    print("CODE", code)
    try:
        token_endpoint = 'https://oauth2.googleapis.com/token'
        token_params = {
        "code" : code,  
        "client_id":client_id,
        "client_secret":client_secret,
        "redirect_uri":"http://localhost:5173/point-de-vente/",
        "grant_type":"authorization_code"
        } 
        response = requests.post(token_endpoint, token_params)
        print(response)
        print("responseBack", response.json())
        return response.json()
    except Exception as e:
        return {"error": "Erreur de connexion", "details": str(e)}
        
