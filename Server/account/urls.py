from django.urls import path, include
from .views import *
from eventManagement.views import RetrieveUpdateAddTickets, ListAddTicketsOrganisateur
urlpatterns = [
    path('login/google/', GoogleLoginGetToken, name="login-google"),
    path('login/', Login.as_view()), #return Token  
    path('register/', RegisterUser.as_view()),
    path('register/<int:pk>', RetrieveUpdateUser.as_view()),

    path('point-de-vente/register', RegisterPDV.as_view()),
    path('point-de-vente/<int:pk>/', UpdatePDV.as_view()),
    path('point-de-vente/', ListPDV.as_view()),
    
    
    #URL Organisateur account/point-de-vente/pk:pdv/slug
    path("point-de-vente/<int:pdvId>/<slug:slug>/list-Addtickets", ListAddTicketsOrganisateur.as_view(), name="list-Addticket-organisateurs"),
    path("point-de-vente/<int:pdvId>/<slug:slug>/update-Addtickets/<int:pk>", RetrieveUpdateAddTickets.as_view(), name="list-Addticket-organisateurs"),

]