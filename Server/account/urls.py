from django.urls import path
from .views import *
from eventManagement.views import RetrieveUpdateAddTickets
urlpatterns = [
    path('login/google/', GoogleLoginGetToken, name="login-google"),
    path('login/', Login.as_view()), #return Token  
    path('point-de-vente/register', RegisterPDV.as_view()),
    path('register/', RegisterUser.as_view()),
    path('register/<int:pk>', RetrieveUpdateUser.as_view()),
    # path('user/', GetUserInfo.as_view()),
    path('logout/', LogoutUser.as_view()),

    #Organisateur
    path('point-de-vente/<int:pdvId>/<slug:slug>/update-Addtickets/<int:pk>', RetrieveUpdateAddTickets.as_view())
]