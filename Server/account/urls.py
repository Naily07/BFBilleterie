from django.urls import path
from .views import *
urlpatterns = [
    path('login/google/', GoogleLoginGetToken, name="login-google"),
    path('login/', Login.as_view()), #return Token  
    path('point-de-vente/register', RegisterPDV.as_view()),
    path('register/', RegisterUser.as_view()),
    path('register/<int:pk>', RetrieveUpdateUser.as_view()),

]