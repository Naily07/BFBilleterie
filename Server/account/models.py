from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import Group, Permission
# Create your models here.

class MyUser(User):
    tel = models.TextField(blank = True)
    account_type = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.username
    
    class Meta():
        verbose_name = "GlobalUser"
                

class PointDeVente(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='pointdevente_groups', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='pointdevente_user_permissions', blank=True
    )
    lieu = models.TextField()
    tel = models.TextField(blank = True, null = True, default = None)
    owner = models.ForeignKey(User, default = 1, on_delete = models.CASCADE, related_name = "pointdevente_related")
    is_active = models.BooleanField(default = False)

    def __str__(self):
        return self.username
    
    class Meta():
        verbose_name = "Revendeur"