from django.shortcuts import render
from requests import Response
from rest_framework import generics
from .models import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.text import slugify
from .serializer import *
from django.http import Http404
from rest_framework import status
from django.db import IntegrityError
# Create your views here.

class ListCreateSponsor(generics.ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class ListCreateEvent(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser

    def create(self, request, *args, **kwargs):
        try :
            serializer = self.get_serializer(data=request.data)
            # image = request.FILES
            spons = request.FILES.getlist('sponsor_image')
            #Recuperation de sponsors image lien
            serializer.is_valid(raise_exception=True)
            if not serializer.is_valid():
                return Response({"Evenement existe déjà"}, status=400)
            
            self.perform_create(serializer)
            currentEvent = serializer.instance

            for image in spons:
                Sponsor.objects.create(
                    image = image,
                    event = currentEvent
                )

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def perform_create(self, serializer):
        try:
            user = self.request.user    
            print("slug", slugify(serializer.validated_data.get('nom')))
            slug = slugify(serializer.validated_data.get('nom'))
            if(not user.is_anonymous):
                serializer.save(owner = user, slug = slug)
            else:
                serializer.save(slug = slug)

        except IntegrityError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RemovEvent(generics.RetrieveDestroyAPIView, generics.ListAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser
    lookup_field = "slug"


class DetailEvent(generics.RetrieveAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser
    lookup_field = "slug"

class CreateListTickets(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerealiser

    def get_queryset(self, *args, **kwargs):
        event = self.get_Oneevent(request=self.request)
        tickets = event.ticket_related.all()
        ticketserial = TicketSerealiser(tickets, many = True).data
        return ticketserial

    def post(self, request, *args, **kwargs):
        get_event = self.get_Oneevent(request=request)
        try:
            type_ticket = request.data.get('type_ticket')
            print("type de ticket", type_ticket)
            ticketExist = Ticket.objects.get(event = get_event, type_ticket = type_ticket)#List de tickets
            return Response(f'Le type de ticket {ticketExist} existe déjà')
        except Ticket.DoesNotExist:
            if get_event :
                #Verification de limite de type de ticket
                ticketList = self.get(request=request).data
                size = len(ticketList)
                if size < 3 :
                    return super().post(request, *args, **kwargs)
                return Response("Limite de ticket atteinte")
            else:
                raise serializers.ValidationError("L'événement spécifié n'a pas été trouvé.")
        
    def perform_create(self, serializer):
        get_event = self.get_Oneevent(request=self.request)
        #Ajout un evenement dans la clé etrangère de Ticket
        serializer.save(event = get_event)             
        return Response(serializer.data, status=201)
        
    def get(self, request, *args, **kwargs):
        get_event = self.get_Oneevent(request=request)
        print(get_event)
        if get_event:
            tickets = Ticket.objects.filter(event = get_event)
            serealiser = TicketSerealiser(tickets, many = True)
            return Response(serealiser.data)
        else:
            return Response({"detail": "L'événement spécifié n'a pas été trouvé."}, status=404)
    
    def get_Oneevent(self, request):
        slug = self.kwargs.get('slug')
        try:
            get_event = Evenement.objects.filter(slug__iexact=slug, owner__exact = self.request.user).first()
            return get_event
        except Evenement.DoesNotExist:
            raise Http404("L'événement spécifié n'a pas été trouvé.")