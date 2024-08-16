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
from rest_framework.views import APIView
from api.mixins import *
from account.serializer import PointDeVenteSerializer
from rest_framework.permissions import IsAuthenticated
from .utils import createQrCode
# Create your views here.

class ListSponsor(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class ListCreateEvent( generics.ListCreateAPIView, OwnerQuerySet, OrganisateursEditorMixin):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser
    # permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        context = super(ListCreateEvent, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def create(self, request, *args, **kwargs):
        try :
            serializer = self.get_serializer(data=request.data)
            image = request.FILES.get('image')
            print(request.data.get('nom'))
            spons = request.FILES.getlist('sponsor_image')
            #Recuperation de sponsors image lien
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({"message":"Evenement existe déjà"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.is_valid(raise_exception=True)
            
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
            print("perform",user)
            print("slug", slugify(serializer.validated_data.get('nom')))
            slug = slugify(serializer.validated_data.get('nom'))
            if(not user.is_anonymous):
                serializer.save(owner = user, slug = slug)
            else:
                print("default user 1 to event")
                serializer.save(slug = slug)

        except IntegrityError as e:
            return Response({"error": f"perform_create {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class ListTypeEvent(generics.ListAPIView, ):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser
    qs_filter_type_event = 'type_event'


class RemovEvent(generics.RetrieveDestroyAPIView, generics.ListAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser
    lookup_field = "slug"


class DetailEvent(generics.RetrieveAPIView, OrganisateursEditorMixin, PointDeVenteEditorMixin):
    queryset = Evenement.objects.all()
    serializer_class = EventSerealiser
    lookup_field = "slug"

    def get_serializer_context(self):
        context = super(DetailEvent, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class ListCreateTickets(generics.ListAPIView):
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
            add = AddTicket.objects.get_or_create(
                type_ticket = instanceTicket.type_ticket,
                event = instanceTicket.event,
                pointdevente = pdv
            )
            print("get_or_create", add)
        nb_tickets = instanceTicket.nb_ticket
        
        from .utils import createQrCode
        i = 1
        try:
            while i <= nb_tickets :
                createQrCode(i, instanceTicket.type_ticket, instanceTicket.event)
                i+=1
        except Exception as e:
            # instanceTicket
            deleteTicket = Ticket.objects.get(instanceTicket).delete()
            print("Deleting", deleteTicket)
            return Response({"message" : "Erreur lors de la creation de ticket"}, status=500)        
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
            if self.request.user.groups.filter(name='organisateurs').exists():
                get_event = Evenement.objects.get(slug__iexact=slug, owner__exact = self.request.user)
            elif  self.request.user.groups.filter(name='clients').exists() : 
                get_event = Evenement.objects.get(slug__iexact=slug)
            else : raise Evenement.DoesNotExist
            return get_event
        except Evenement.DoesNotExist:
            raise Http404("L'événement spécifié n'a pas été trouvé.")

class BulkCreateTicket(APIView, OrganisateursEditorMixin):

    def post(self, request, *args, **kwargs):
        listTicket = request.data
        listInstanceTicket = []
        print("LIST ", listTicket)
        try:
            get_event = self.get_Oneevent(request=request)
            for ticket in listTicket:
                ticketExist = Ticket.objects.filter(event = get_event, type_ticket = ticket['type_ticket'])#List de tickets
                if ticketExist:
                    return Response(f'Le type de ticket {ticketExist} existe déjà')
                print(ticket)
                if get_event :
                    #Verification de limite de type de ticket
                    tickets = Ticket.objects.filter(event = get_event)
                    listTicket = TicketSerealiser(tickets, many = True).data
                    size = len(listTicket)
                    if size > 3 :
                        return Response("Limite de ticket atteinte", status=status.HTTP_406_NOT_ACCEPTABLE)
                print("DATA ", request.data)
                listInstanceTicket.append(Ticket(**ticket, event = get_event))
            ticketData = Ticket.objects.bulk_create(listInstanceTicket)
            #Creation de AddTicket
            owner = CustomUser.objects.filter(username = self.request.user).first()
            print("Ornganisateurs Tickets", owner)
            list_pdv = owner.pointdevente_related.all()
            for instance in listInstanceTicket :
                for pdv in list_pdv:
                    print(pdv)
                    add, isCreated = AddTicket.objects.get_or_create(
                        type_ticket = instance.type_ticket,
                        event = instance.event,
                        prix = instance.prix,
                        pointdevente = pdv
                    )
                    print("get_or_create", add, isCreated)
                    nb_tickets = int(instance.nb_ticket)
                    try:
                        i = 1
                        while i <= nb_tickets :
                            createQrCode(i, instance.type_ticket, instance.event)
                            i+=1
                    except Exception as e:
                        # instanceTicket
                        deleteTicket = Ticket.objects.get(instance).delete()
                        print("Deleting", deleteTicket)
                        return Response({"message" : "Erreur lors de la creation de QRticket"}, status=500)        
            return Response(TicketSerealiser(ticketData, many = True).data, status=201)
        except Exception as e:
            raise BaseException(e)
    
    def get_Oneevent(self, request):
        slug = self.kwargs['slug']
        try:
            get_event = Evenement.objects.get(slug__iexact=slug, owner__exact = self.request.user)
            return get_event
        except Evenement.DoesNotExist:
            raise Http404("L'événement spécifié n'a pas été trouvé.")
        
class UpdateTickets(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerealiser

    def perform_update(self, serializer):
        serializer.save()
        instance = serializer.instance
        updateNumber = instance.nb_ticket
        print(instance.id)
        try :
            qr = TicketQrCode.objects.filter(id__iexact = instance.id).last()
            print("QR", qr)
            if qr :
                if updateNumber > qr.num :
                    i = qr.num
                    from .utils import createQrCode
                    while i < updateNumber:
                        i += 1
                        createQrCode(instance.id, i, instance.type_ticket, instance.event)
        except TicketQrCode.DoesNotExist:
            print("Pas de Qr Code pour l'instant")

class DeleteTicket(generics.DestroyAPIView, generics.RetrieveAPIView, OrganisateursEditorMixin):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerealiser

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            event = self.get_Oneevent(request=request)
            Ticket.objects.get(event = event, type_ticket = instance.type_ticket)
            AddTicket.objects.delete(event = event, type_ticket = instance.type_ticket)
            self.perform_destroy(instance)
        except Ticket.DoesNotExist:
            raise Http404("Le Ticket spécifié n'a pas été trouvé.")
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        deleteAddTicket = AddTicket.objects.filter(event__exact = instance.event, type_ticket__iexact=instance.type_ticket).delete()
        print("DeleteADD ", deleteAddTicket)
        return super().perform_destroy(instance)
    
    def get_Oneevent(self, request):
        slug = self.kwargs.get('slug')
        try:
            get_event = Evenement.objects.get(slug__iexact=slug, owner__exact = self.request.user)
            print("SLUG", get_event)
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

class BulkUpdateAddTickets(OrganisateursEditorMixin, AddTicketQuerySet, generics.GenericAPIView,):
    # qs_field_pdv = 'pk' #Point de vente dans l'url, cible pour avoir le AddTicket
    queryset = AddTicket.objects.all()
    serializer_class = AddTicketSerializer
    lookup_field = 'pk'
    qs_field = 'pdvId'

    def patch(self, request, *args, **kwargs):
        try:
            datas = request.data
            for data in datas:
                addTicket = AddTicket.objects.get(id=data['pk'])
                serializer = self.get_serializer(addTicket, data=data)
                sommeAddTicket = addTicket.nb_ticket - int(data['nb_ticket'])
                ticket = Ticket.objects.get(event = addTicket.event, type_ticket = addTicket.type_ticket)
                print("TT", addTicket.nb_ticket)
                if sommeAddTicket < 0 :
                    ticket.nb_ticket += sommeAddTicket
                    if ticket.nb_ticket < 0:
                        return Response({"message" : "Erreur sur la quantité"}, status=status.HTTP_400_BAD_REQUEST)
                    ticket.save()
                elif sommeAddTicket > 0 :
                    ticket.nb_ticket += sommeAddTicket
                    ticket.save()
                if sommeAddTicket != 0:
                    addTicket.nb_ticket = data['nb_ticket']
                    addTicket.save()
                # raise serializer.
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AddTicket.DoesNotExist:
            print("Does")
            raise Http404
        except Exception as e:
            raise BaseException(e)


from rest_framework.views import APIView
from .models import TicketQrCode
class ScanQrCode(OrganisateursEditorMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            print(self.kwargs)
            type_ticket = kwargs['type_ticket']
            num = kwargs['num']
            event_slug = kwargs['slug']
            event = Evenement.objects.filter(slug__iexact = event_slug).first()
            if not event:
                return Response({"detail" : "Evenement n'exist pas"}, status=status.HTTP_400_BAD_REQUEST)
            ticketQrCode = TicketQrCode.objects.filter(type_ticket = type_ticket, num = num , event = event).first()
            if ticketQrCode and not ticketQrCode.is_disabled:
                ticket = Ticket.objects.get(event__exact = event, type_ticket__iexact = type_ticket)
                ticketSerializer = TicketSerealiser(ticket)
                ticketQrCode.is_disabled = True
                return Response(ticketSerializer.data, status=status.HTTP_200_OK)
        except (TicketQrCode.DoesNotExist, Ticket.DoesNotExist):
            raise Http404('Le ticket n\'exist pas')
        except Exception as e:
            raise BaseException(e)

class ListQrCode(generics.ListAPIView, OwnerQuerySetQrCode):
    queryset = TicketQrCode.objects.all()
    serializer_class = TicketQrCodeSerialiser

class RetrieveQrCode(generics.RetrieveAPIView):
    queryset = TicketQrCode.objects.all()
    serializer_class = TicketQrCodeSerialiser

class BuyTicket(APIView, ClientEditorMixin):
    def post(self, request,* args, **kwargs):
        user = request.user
        datas = request.data
        for data in datas:
            type_ticket = data['type_ticket']
            nb_ticket = int(data['nb_ticket'])
            try:
                slug = self.kwargs['slug']
                event = Evenement.objects.get(slug = slug)
                ticket = Ticket.objects.filter(event = event, type_ticket = type_ticket).first()

                if ticket is None:
                    return Response({'detail': 'Ticket type not found'}, status=status.HTTP_404_NOT_FOUND)

                # Vérifier la disponibilité des tickets
                if ticket.nb_ticket < nb_ticket:
                    return Response({'detail': 'Not enough tickets available'}, status=status.HTTP_400_BAD_REQUEST)
                
                listQrCode = TicketQrCode.objects.filter(addOwner__exact = None, type_ticket__iexact = type_ticket, event__exact = event)[:nb_ticket]
                instanceQrCodeList = []
                for qrCodeinstance in listQrCode:
                    qrCodeinstance.addOwner = user
                    instanceQrCodeList.append(qrCodeinstance)
                TicketQrCode.objects.bulk_update(instanceQrCodeList, ['addOwner'])
                ticket.nb_ticket -= nb_ticket
                ticket.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Evenement.DoesNotExist :
                return Response({"message" : "Evenement not Found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                raise BaseException(e)