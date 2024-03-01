from django.urls import path
from .views import *
urlpatterns = [
    path('login/google/', GoogleLoginGetToken, name="login-google"),
    path('login/', LoginPDV.as_view())
]