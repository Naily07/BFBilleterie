from django.urls import path
from .views import *
urlpatterns = [
    path("create-list-event/", ListCreateEvent.as_view(), name="list-event"),
    path("<slug:slug>/", DetailEvent.as_view(), name="detail-event"),
    path("remove-event/<slug:slug>/", RemovEvent.as_view(), name="delete-event"),
    path("<slug:slug>/tickets", ListCreateTickets.as_view(), name="list-ticket"),
    path("<slug:slug>/update-ticket/<int:pk>", UpdateTickets.as_view(), name="update-ticket"),
    path("list-sponsors/", ListSponsor.as_view(), name="list-sponsor"),

    #Vue PDV
    path("<slug:slug>/list-Addtickets", ListAddTicketsPDV.as_view(), name="list-Addticket-pointdevente"),
    
    #Scan Code
    path("<slug:slug>/ticket/<str:type_ticket>/<int:num>", ScanQrCode.as_view(),),

]
