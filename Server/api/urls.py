from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *
urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/', TokenActivateView.as_view(), name='token_activate'),    #Activation compte token
]