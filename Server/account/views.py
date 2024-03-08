from datetime import timedelta
from django.conf import settings
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics
from rest_framework.response import Response
from .utils import GoogleLoginGetToken, GoogleGetUserInfo
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from api.serializer import MyTokenAuthentication
# Create your views here.


class Login(APIView):

    def post(self, request):
        # code = request.data.get('code')
        # token = GoogleLoginGetToken(code)
        # items = token.items()
        # token = ""
        # error = ""
        # for key, value in items:
        #     if key == "access_token":
        #         token = value
        #         break
        #     if key == "error":
        #         error = value
        #         break
        # print("Acces", token)

        # userInfo = GoogleGetUserInfo(access_token)

        username = request.data.get('username')#Login Google
        email = request.data.get('email')#Login Google
        user = PointDeVente.objects.filter(email__iexact = email).first()
        try :
            if user is None :
                raise AuthenticationFailed("le compte n'existe pas")
            if user:
                if user.is_active == False:
                    access, refresh = MyTokenAuthentication.get_token(user)
                    user.username = username
                    user.is_active = True
                    if access & refresh :
                        user.save()
                    return Response({"access_token": access, "refresh_token": access}, status=status.HTTP_200_OK)    
            # if user:
            #     access, refresh = MyTokenAuthentication(user)
        except Exception as e:
            raise AuthenticationFailed(f"Login error {e} ")
        return Response({"ok"})
        #Get information user
        # pdv = PointDeVente.objects.get_or_create()
        # if access:
        #     return Response({"access_token": access,"refresh_token":refresh }, status=status.HTTP_200_OK)    
        # elif error :
        #     return Response({"Error" : error})

from eventManagement.models import Evenement, PointDeVenteToEvenement, Ticket, AddTicket
from api.serializer import MyTokenActivation
from django.core.mail import send_mail, EmailMultiAlternatives

class RegisterPDV(generics.ListCreateAPIView):
    queryset = PointDeVente.objects.all()
    serializer_class = PointDeVenteSerializer

    def post(self, request, *args, **kwargs):
        #Creation token sur les données entrer par l'organisateurs
        email = request.data.get('email')
        owner = request.user
        list_event = request.data.get('list_event')
        lieu = request.data.get('lieu')
        token = MyTokenActivation.get_token(owner, email, list_event, lieu)
            # access_token = token['access_token']
        print(request.method)
        if request.method == "POST" :
        #     backEndUrl = settings.BACKEND_URL
        #     activation_link = f"{backEndUrl}/api/token/activate?token={token}"
        #     subject = "Accepter l'invitation de l'organisateur"
        #     message = f"accepter l'invation {activation_link}"
        #     from_email = 'leonelheri25@gmail.com'
            # plain_message = (message)
            # send_mail(subject = subject, message = message, from_email = from_email, recipient_list = [email])
            return Response({"message": "Un e-mail d'activation a été envoyé avec succès."}, status=status.HTTP_201_CREATED)
    
    def put(self, request, *args, **kwargs):
        print("DATAS", *args)
        datas = args[0]
        for key, value in datas.items():
            request.data[key] = str(value)
            print(key) 
        request.data['username'] = 'zzz'
        list_event = request.data.get('list_event')
        print("request", request.data.get('lieu'))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        listEventInstance = []
        for event in list_event:
            eventinst = Evenement.objects.filter(nom__iexact = event).first()
            listEventInstance.append(eventinst)
            if not eventinst:
                return Response({f"L'evenement {event} n'existe pas"})
        try :
            if PointDeVente.objects.filter(username__iexact = nom_pdv, owner__exact = request.user):
                #cas de même organisateur sur même pdv
                return Response({"le point de vente est invalide ou existe deja"})
            elif not PointDeVente.objects.filter(username__iexact = nom_pdv):
                #username field existe dans la base => NOT
                #cas d'un autre organisateur et pdv n'est pas encore dans la base
                print("Passage a la creation")
                self.perform_create(serializer)   
        except Exception as e:
            return Response({"error" : "Une erreur s'est produit"})
        # Cas de pdv deja en base
        # currentpdv = PointDeVente.objects.filter(username__iexact = nom_pdv, owner__exact = request.user).first()
        currentpdv = serializer.instance
        print("ListEvenetInst", listEventInstance)
        print("CurrentPDV", currentpdv)

        for event in listEventInstance:
            print("ListEvenetInst", event)
            print("CurrentPDV", currentpdv)
            try:
                if event and currentpdv:
                    PointDeVenteToEvenement.objects.create(event = event, pdv = currentpdv)
                    #recuperation du ticket de reffernce
                    ticket = Ticket.objects.filter(event__exact = event, owner__exact = request.user).first()
                    print("Le ticket de ref", ticket)
                    AddTicket.objects.create(
                        type_ticket = ticket.type_ticket,
                        nb_ticket = 0,
                        event = ticket.event,
                        owner = ticket.owner,
                        pointdevente = currentpdv)
                    print('create PDVToEvent')
                else :
                    return Response({f"L'evenement {event} n'existe pas ou le pdv n'est pas specifié"})
            except Exception as e:
                return Response({f"erreur sur les données {e} "}, status=400)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    def perform_create(self, serializer):
        owner_id = serializer.validated_data.get('user_id')
        serializer.save(owner = owner_id)


    def create(self, request, *args, **kwargs):
        print("DATAS", *args)
        datas = args[0]
        try:
            print("aa")
            for key, value in datas.items():
                request.data[key] = (value)
                print(value) 
            list_event =request.data.get('list_event')
            request.data['username'] = "MyUsername"
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            owner = serializer.validated_data.get('user_id')
            listEventInstance = []
            print("CREATION", list_event)
        except Exception as e :
            return {f"exception {e}"}
        for event in list_event:
            print("evv", event)
            eventinst = Evenement.objects.filter(nom__iexact = event).first()
            listEventInstance.append(eventinst)
            if not eventinst:
                return Response({"message" : f"L'evenement {event} n'existe pas"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try :
            if PointDeVente.objects.filter(email__iexact = email, owner__exact = owner):
                #cas de même organisateur sur même pdv
                return Response({"message" :"le point de vente est invalide ou email existe deja"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
            self.perform_create(serializer)
        except Exception as e:
            print("inexistant")
            return Response({"error" : f"Une erreur s'est produit {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        print("CREATION")
        self.perform_create(serializer)
        # Cas de pdv deja en base
        # currentpdv = PointDeVente.objects.filter(username__iexact = nom_pdv, owner__exact = request.user).first()
        currentpdv = serializer.instance
        print("ListEvenetInst", listEventInstance)
        print("CurrentPDV", currentpdv)

        for event in listEventInstance:
            print("ListEvenetInst", event)
            print("CurrentPDV", currentpdv)
            try:
                if event and currentpdv:
                    PointDeVenteToEvenement.objects.create(event = event, pdv = currentpdv)
                    #recuperation du ticket de reffernce
                    ticket = Ticket.objects.filter(event__exact = event).first()
                    print("Le ticket de ref", ticket)
                    AddTicket.objects.create(
                        type_ticket = ticket.type_ticket,
                        nb_ticket = 0,
                        event = ticket.event,
                        pointdevente = currentpdv)
                    print('create PDVToEvent')
                else :
                    return Response({f"L'evenement {event} n'existe pas ou le pdv n'est pas specifié"})
            except Exception as e:
                return Response({f"erreur sur les données {e} "}, status=400)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

            