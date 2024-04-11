from typing import Tuple
from django.conf import settings
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token

class CustomJWT(JWTAuthentication):

    def authenticate(self, request: Request):
        header = self.get_header(request)
        raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        if header is None :
            print('Head None')
            return None
        else:
            print("SET RAW To Head")
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None
                
        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token