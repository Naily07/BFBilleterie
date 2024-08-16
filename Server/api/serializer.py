from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import Token
from datetime import timedelta
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt import exceptions


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
        token_data['account_type'] = user.account_type
        token_data['pk'] = user.pk
        print(user.account_type)
        token_data['email'] = user.email
        access = token_data.access_token
        refresh = token_data
        
        return access, refresh

class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None
    def validate(self, attrs) :
        attrs['refresh'] = self.context['request'].COOKIES.get("refresh")
        print("Attr", self.context['request'].COOKIES.get("refresh"))
        try :
            if attrs['refresh']:
                return super().validate(attrs)
        except :
            raise exceptions.InvalidToken('Refresh Token invalid')