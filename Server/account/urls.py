from django.urls import path
from .views import *
urlpatterns = [
    path('login/google/', GoogleLoginGetToken, name="login-google"),
    path('login/', Login.as_view()),
    path('register/point-de-vente', RegisterPDV.as_view()),
]