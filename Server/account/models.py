from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


class PointDeVente(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='pointdevente_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='pointdevente_user_permissions'
    )
    lieu = models.TextField()
    contact = models.TextField()
    
    def __str__(self) -> str:
        return self.username

class Orgnisateur(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='organisateur_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='organisateur_user_permissions'
    )
    def __str__(self) -> str:
        return self.username