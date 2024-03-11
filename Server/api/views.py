from django.shortcuts import render
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.tokens import Token
from rest_framework.views import APIView
from api.utils import decodeToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import jwt
from rest_framework_simplejwt.settings import api_settings
# Create your views here.

from account.views import RegisterPDV
from account.models import PointDeVente
from account.serializer import PointDeVenteSerializer
from rest_framework.generics import ListCreateAPIView
from account.models import MyUser

class TokenActivateView(ListCreateAPIView):
    queryset = PointDeVente.objects.all()
    serializer_class = PointDeVenteSerializer

    def perform_create(self, serializer):
        owner_id = self.request.data.get('user_id')
        username = self.request.data.get('username')
        if not username:
            email = serializer.validated_data.get('email')
            username = email.split('@')[0]
        owner = MyUser.objects.filter(id__iexact = owner_id).first()
        if owner :
            print("IDD", owner)
            serializer.save(owner = owner, username = username)
        return Response({"Error" : "Not Save"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request):
        token = (request.query_params.get('token'))
        print("get", token)
        try:
            # mytoken = TokenVerifyView.
            decoded_token = jwt.decode(token, api_settings.SIGNING_KEY, algorithms=[api_settings.ALGORITHM])
            print("isVerifier", decoded_token)
            result = RegisterPDV.create(self, request, decoded_token)
            print("Result", result)
            if (result.status_code == 200) | (result.status_code == 201):
                return RegisterPDV.get(self, request)
            return result
        except Exception as e:
            print("Error", e)        
            return Response({"error" : f"createPDV {e}"})