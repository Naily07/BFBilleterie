from django.urls import path
from .views import *
urlpatterns = [
    path("create-list-event/", ListCreateEvent.as_view(), name="list-event"),
    path("create-list-event/<slug:slug>/", DetailEvent.as_view(), name="detail-event"),
    path("remove-event/<slug:slug>/", RemovEvent.as_view(), name="delete-event"),
    path("create-list-event/<slug:slug>/tickets", ListCreateTickets.as_view(), name="list-ticket"),
    path("create-list-spons/", ListCreateSponsor.as_view(), name="list-sponsor"),
    # path("create-list-spons/", ListCreateSponsor.as_view(), name="list-sponsor"),
    path("<slug:slug>/list-Addtickets/", ListAddTickets.as_view(), name="list-Addticket"), #AddTicket PointDevente
]
#Dans le point de vente on a une liste d'event avec lien AddTickets
# {
#     "nom": "soiré",
#     "slug": "soire"
# }