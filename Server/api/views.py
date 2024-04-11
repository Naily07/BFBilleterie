from django.shortcuts import render
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.tokens import Token
from api.utils import decodeToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import jwt
from rest_framework_simplejwt.settings import api_settings
from .serializer import CookieTokenRefreshSerializer
# Create your views here.

from account.views import RegisterPDV
from account.models import PointDeVente
from account.serializer import PointDeVenteSerializer
from account.models import CustomUser
from django.contrib.auth.models import Group
from django.conf import settings

class CookieRefreshTokenView(TokenVerifyView):
    serializer_class = CookieTokenRefreshSerializer
    
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            refresh = response.data.get('refresh')
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                value= refresh,
                expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'], 
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'], 
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                domain=settings.SIMPLE_JWT['AUTH_COOKIE_DOMAINE'],
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)
    
class TokenActivateView(generics.ListCreateAPIView):
    queryset = PointDeVente.objects.all()
    serializer_class = PointDeVenteSerializer

    def perform_create(self, serializer):
        try :
            print(serializer.validated_data)
            owner_id = self.request.data.get('user_id')
            owner = CustomUser.objects.filter(id__iexact = owner_id).first()
            username = serializer.validated_data.get('username')
            account_type = "pointdevente"
            print("NAME", username)
            if owner and username :
                print("IDD", serializer.validated_data)
                serializer.save(owner = owner, username = username, account_type = account_type )
                pdv = serializer.instance
                group = Group.objects.get(name = f"{account_type}s")
                # if not pdv.groups.filter(name = group.name).exists():
                if group:
                    pdv.groups.add(group)
                else:
                    return Response({"Error" : f"Atribution de {account_type} group"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # return Response({"Error" : "Not Save"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            raise e

    def get(self, request):
        token = (request.query_params.get('token'))
        print("get", token)
        try:
            # mytoken = TokenVerifyView.
            decoded_token = jwt.decode(token, api_settings.SIGNING_KEY, algorithms=[api_settings.ALGORITHM])
            print("isVerifier", decoded_token)
            result = RegisterPDV.create(self, request, decoded_token)
            print("Result", result)
            # if (result.status_code == 200) | (result.status_code == 201):
            #     return RegisterPDV.get(self, request)
            return result
        except Exception as e:
            print("Error", e)        
            return Response({"error" : f"createPDV {e}"})