from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.http import HttpRequest
from .models import PointDeVente, MyUser

class PointDeVenteBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Rechercher l'utilisateur par email
        email = kwargs.get('email')
        print("GET Email", email)
        try:
            user = PointDeVente.objects.get(username=username, email = email)
        except PointDeVente.DoesNotExist:
            return None

        # Vérifier le mot de passe
        # if user.check_password(password):
        #     return user
        
        return user
    
class MyUserAuthenticationBack(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any):
        email = kwargs.get('email')
        print("Emm", email)
        print("OKKA")
        try:
            user = MyUser.objects.get(username = username, email = email)
        
        except MyUser.DoesNotExist:
            return None
        
        return user

class UserAuthenticationBack(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any):
        print("OKKO")
        try:
            user = User.objects.get(username = username)

        except User.DoesNotExist:
            return None
    
        # Vérifier le mot de passe
        if user.check_password(password):
            return user
        
        return None