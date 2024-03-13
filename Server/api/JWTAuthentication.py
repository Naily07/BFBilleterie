from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AbstractUser, User
from account.models import PointDeVente

from django.contrib.auth import get_user_model

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Spécifiez directement le nom du modèle ici

        # Récupérer le modèle d'utilisateur spécifié
        # print(self.user_model)
        UserModel = get_user_model()

        try:
            if super().authenticate(request):
                # self.user_model  = get_user_model 
                return super().authenticate(request)
            # if super().authenticate(request):
            #     print("MOD1")
            # else:
            # Configurer dynamiquement les relations de clé étrangère
            # Appeler la méthode authenticate de la classe parente
        except Exception :
            try :
                UserModel = get_user_model()
                self.user_model = PointDeVente
                UserModel._meta.get_field('groups').remote_field.model = self.user_model
                UserModel._meta.get_field('user_permissions').remote_field.model = self.user_model
                return super().authenticate(request)
            except Exception as e:
                return None
            # Gérer l'erreur si le modèle d'utilisateur spécifié n'existe pas
        return None
        
