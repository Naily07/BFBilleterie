from django.shortcuts import render
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
from api.mixins import OrganisateursEditorMixin, UserQuerySet, PointDeVenteEditorMixin
from account.serializer import PointDeVenteSerializer
# Create your views here.

class ListSponsor(OrganisateursEditorMixin, generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class ListCreateEvent(OrganisateursEditorMixin, UserQuerySet, generics.ListCreateAPIView):
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
                return Response({"message":"Evenement existe déjà"}, status=status.HTTP_400_BAD_REQUEST)
            
            self.perform_create(serializer)
            currentEvent = serializer.instance
            #Creation direct de tickets
            # ListTCreateickets().post(self, request=request)
            
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
                print("default user 1 to event")
                serializer.save(slug = slug)

        except IntegrityError as e:
            return Response({"error": f"perform_create {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class RemovEvent(OrganisateursEditorMixin, UserQuerySet, generics.RetrieveDestroyAPIView, generics.ListAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser
    lookup_field = "slug"


class DetailEvent(OrganisateursEditorMixin, UserQuerySet, generics.RetrieveAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser
    lookup_field = "slug"


class ListCreateTickets(OrganisateursEditorMixin, generics.ListCreateAPIView):
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
        #Ajout AddTicket to Pdv
        owner = CustomUser.objects.filter(username = self.request.user).first()
        print("owner Tickets", owner)
        instanceTicket = serializer.instance
        list_pdv = owner.pointdevente_related.all()

        for pdv in list_pdv:
            print(pdv)
            AddTicket.objects.get_or_create(
                type_ticket = instanceTicket.type_ticket,
                event = instanceTicket.event,
                pointdevente = pdv
            )
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



#POINTDEVENTE
from api.mixins import AddTicketQuerySet
class ListAddTicketsPDV(PointDeVenteEditorMixin, AddTicketQuerySet, generics.ListAPIView):
    queryset = AddTicket.objects.all()
    serializer_class = AddTicketSerializer

    def add_qs_field_user(self):
        pdv = self.request.user
        pdv = PointDeVente.objects.filter(username__iexact = pdv).first()
        print(pdv.owner)
        return pdv.owner 


#Organisateur 
class ListAddTicketsOrganisateur(OrganisateursEditorMixin, AddTicketQuerySet, generics.ListCreateAPIView):
    queryset = AddTicket.objects.all()
    serializer_class = AddTicketSerializer    
    # qs_field_pdv = 'pk' #Point de vente dans l'url, cible pour avoir le AddTicket
    qs_field_event = 'slug'

class RetrieveUpdateAddTickets(OrganisateursEditorMixin, AddTicketQuerySet, generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = AddTicket.objects.all()
    serializer_class = AddTicketSerializer    
    lookup_field = 'pk'
    qs_field = 'pdvId'

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        serializer.save()
        addTicket = serializer.instance
        ticket = Ticket.objects.get(event = addTicket.event, type_ticket = addTicket.type_ticket)
        ticket.nb_ticket -= addTicket.nb_ticket
        ticket.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        pdv = self.get_object().pointdevente
        serializer = self.get_serializer(instance)
        print("Data", serializer.data)
        return Response(serializer.data)