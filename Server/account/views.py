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
        user =  User.objects.filter(email__iexact = email).first() 
        pdv = PointDeVente.objects.filter(email__iexact = email).first()
        # print("GRR : ", group)
        getUser = object()
        try :
            if user is None  and pdv is None:
                raise AuthenticationFailed("le compte n'existe pas")
            if pdv:
                #POINT DE VENTE
                print("GERRR  : ", pdv.groups.all())
                if pdv.is_active == False:
                    pdv.is_active = True
                    pdv.username = username
                    pdv.save()
                getUser = pdv
            else :
                print("Group  : ", user.groups.all())
                getUser = user
            access, refresh = MyTokenAuthentication.get_token(getUser)
            response = Response()
            # print(token)
            # response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                "access_token": f"{access}",
                "refresh_token": f"{refresh}"
            }
            response.status_code = status.HTTP_200_OK
            return response  
        except Exception as e:
            raise AuthenticationFailed(f"Login error {e}")
        
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
    
    #Mbola ts nokitihana
    def put(self, request, *args, **kwargs):
        print("DATAS", *args)
        datas = args[0]
        for key, value in datas.items():
            request.data[key] = str(value)
            print(key) 
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
    


    def create(self, request, *args, **kwargs):
        print("DATAS", *args)
        datas = args[0]
        serializer = self.get_serializer(data=request.data)
        try:
            for key, value in datas.items():
                request.data[key] = (value)
                # print(value) 
            list_event =request.data.get('list_event')
            serializer.is_valid(raise_exception=True)
            owner_id = request.data.get('user_id')
            email = serializer.validated_data.get('email')
            username = email.split('@')[0] 
            owner = MyUser.objects.filter(id__iexact = owner_id).first()
            serializer.validated_data['username'] = username
            print("OWN", owner, owner_id, email)
            listEventInstance = []
        except Exception as e :
            return Response({f"exception {e}"})
        if list_event:
            for event in list_event:
                print("evv", event)
                eventinst = Evenement.objects.filter(nom__iexact = event).first()
                listEventInstance.append(eventinst)
                if not eventinst:
                    return Response({"message" : f"L'evenement {event} n'existe pas"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            if PointDeVente.objects.filter(email__iexact = email, owner__exact = owner).first():
                #cas de même organisateur sur même pdv
                return Response({"message" :"le point de vente est invalide ou email existe deja"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
        except Exception as e:
            return Response({"error" : f"Une erreur s'est produit {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        try:
            self.perform_create(serializer)
            print("Crée", serializer.data)
        except Exception as e:
            return Response({"message": f" Invalid Data {e}"}, status=status.HTTP_400_BAD_REQUEST)
        # Cas de pdv deja en base
        # currentpdv = PointDeVente.objects.filter(username__iexact = nom_pdv, owner__exact = request.user).first()
        currentpdv = serializer.instance
        print("ListEvenetInst", listEventInstance)
        print("CurrentPDV", currentpdv)

        if listEventInstance:
            for event in listEventInstance:
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
                        return Response({f"L'evenement {event} n'existe pas ou le pdv n'est pas specifié"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except Exception as e:
                    return Response({f"erreur sur les données {e} "}, status=400)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

from .serializer import UserSerialiser
class RegisterUser(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerialiser

    def post(self, request, *args, **kwargs):
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
        return self.create(request, *args, **kwargs)

        
class RetrieveUpdateUser(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerialiser
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def perform_update(self, serializer):
        account_type = serializer.validated_data.get('account_type')
        try:
            group = Group.objects.get(name = f"{account_type}s")
            userInstance = serializer.instance
            if userInstance.groups is None:
                print("ADD")
                userInstance.groups.add(group)

            print("Group", group)
            print("userInstance", userInstance)
            serializer.save()
        except Exception as e:
            return Response({"message" : f"Groupe {account_type} n'existe pas "}) 