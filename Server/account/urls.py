from django.urls import path
from .views import *
urlpatterns = [
    path('login/google/', GoogleLoginRedirectView.as_view(), name="login-google"),
    path('', LoginPDV.as_view())
]