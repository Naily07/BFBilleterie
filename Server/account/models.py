from typing import Any
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission
# Create your models here.

    
class CustomUserManager(UserManager):
    def _create_user(self, username: str, email: str , password: str | None, **extra_fields: Any):
        if not email:
            raise ValueError("You have enter an invalide email")
        email = self.normalize_email(email)
        user = self.model(email=email, username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.save()
        return user
    
    def create_user(self, username: str, email: str | None = ..., password: str | None = ..., **extra_fields: Any) -> Any:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username: str, email: str | None, password: str | None, **extra_fields: Any):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, email, password, **extra_fields)

        
    
from django.utils import timezone
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank = True, default = '', unique = True)
    sub = models.CharField(null = True, default = None, unique=True, max_length=50)
    username = models.CharField(max_length = 255, blank = True, default = '', unique = True)
    tel =  models.CharField(max_length = 50, blank = True, null = True, default = None)
    name = models.CharField(max_length = 255, blank = True, default = '')
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    date_joined = models.DateTimeField(default = timezone.datetime.now)
    last_login = models.DateTimeField(null = True, blank = True)
    account_type = models.CharField(max_length = 25, default = None, blank = True, null = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username
    
    def get_id(self):
        return self.id
    
class PointDeVente(CustomUser):
    lieu = models.CharField(max_length = 50, blank = True)
    owner = models.ForeignKey(CustomUser, default = 1, on_delete = models.CASCADE, related_name = "pointdevente_related")

