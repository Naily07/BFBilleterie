from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.tokens import Token
from datetime import timedelta
from rest_framework_simplejwt.settings import api_settings

class MyTokenActivation(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user, email, list_event, lieu):
        token_data = super().get_token(user)
        access = token_data.access_token
        access['owner'] = user.username
        access['email'] = email
        access['list_event'] = list_event
        access['lieu'] = lieu

        access.__setitem__('lifetime', str(timedelta(minutes=10)))  
        token = str(access)
        print(token)
        return access

class MyTokenAuthentication(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token_data = super().get_token(user)
        token_data['username'] = user.username
        token_data['email'] = user.email
        access = token_data.access_token
        refresh = token_data
        return access, refresh