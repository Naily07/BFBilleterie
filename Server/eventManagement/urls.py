from django.urls import path
from .views import *
urlpatterns = [
    path("create-list-event/", ListCreateEvent.as_view()),
    path("create-list-event/<slug:slug>/", DetailEvent.as_view()),
    path("remove-event/<slug:slug>/", RemovEvent.as_view()),
    path("create-list-event/<slug:slug>/tickets", CreateListTickets.as_view()),
    path("create-list-spons/", ListCreateSponsor.as_view())
]