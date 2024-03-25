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
        try :
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
            # userInfo = GoogleGetUserInfo(token)
            # print(userInfo)
            sub = request.data.get('sub')#Login Google
            email = request.data.get('email')#Login Google
            # sub = userInfo['sub']
            # email = userInfo["email"]
        except Exception as e:
            raise BaseException(e)
        
        user =  CustomUser.objects.filter(email__iexact = email, sub__iexact = sub).first() 
        if user is None:
            #First connexion
            user = PointDeVente.objects.filter(email__iexact = email).first()
            if user and user.is_active == False:
                user.is_active = True
                user.sub = sub
                user.save()

        print("EOO", user, sub, email)
        try :
            if user is None :
                raise AuthenticationFailed("le compte n'existe pas")

            access, refresh = MyTokenAuthentication.get_token(user)
            response = Response()
            # response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                "access_token": f"{access}",
                "refresh_token": f"{refresh}"
            }
            response.status_code = status.HTTP_200_OK
            return response  
        except Exception as e:
            raise AuthenticationFailed(f"Login error {e}")
 
    

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

        if request.method == "POST" :
            # backEndUrl = settings.BACKEND_URL
            # activation_link = f"{backEndUrl}/api/token/activate?token={token}"
            # subject = "Accepter l'invitation de l'organisateur"
            # message = f"accepter l'invation {activation_link}"
            # from_email = 'leonelheri25@gmail.com'
            # plain_message = (message)
            # send_mail(subject = subject, message = message, from_email = from_email, recipient_list = [email])
            return Response({"message": "Un e-mail d'activation a été envoyé avec succès."}, status=status.HTTP_201_CREATED)

    
    def create(self, request, *args, **kwargs):
        print("DATAS", *args)
        datas = args[0]
        try:
            for key, value in datas.items():
                request.data[key] = (value)
                # print(value) 
            email = request.data.get('email')
            username = email.split('@')[0] 
            request.data['username'] = username
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(request.data)
            list_event = request.data.get('list_event')
            print(list_event)
            owner_id = request.data.get('user_id')
            owner = CustomUser.objects.get(id = owner_id)
            print("OWN", owner, owner_id, email)
            listEventInstance = []
        except Exception as e :
            return Response({f"exception {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if list_event:
            for event in list_event:
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
                    if currentpdv is not None:
                        PointDeVenteToEvenement.objects.create(event = event, pdv = currentpdv)
                        #recuperation du ticket de reffernce
                        try:
                            tickets = event.ticket_related.all()
                            print("TIKK", tickets)
                            for ticket in tickets:
                                print("Le ticket de ref", ticket)
                                AddTicket.objects.create(
                                    type_ticket = ticket.type_ticket,
                                    nb_ticket = 0,
                                    event = ticket.event,
                                    pointdevente = currentpdv)
                                print('create PDVToEvent')
                        except Ticket.DoesNotExist:
                            print(f"les tickets {tickets} n'exist pas")
                    else :
                        return Response({f"L'evenement {event} n'existe pas ou le pdv n'est pas specifié"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except Exception as e:
                    return Response({f"erreur sur les données {e} "}, status=400)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UpdatePDV(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = PointDeVente.objects.all()
    serializer_class = PointDeVenteSerializer
    lookup_field = 'pk'


class ListPDV(generics.ListAPIView):
    queryset = PointDeVente.objects.all()
    serializer_class = PointDeVenteSerializer

from .serializer import UserSerialiser
class RegisterUser(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerialiser

    def post(self, request, *args, **kwargs):
        try:    
            code = request.data.get('code')
            token = GoogleLoginGetToken(code)
            items = token.items()
            token = ""
            error = ""
            for key, value in items:
                if key == "access_token":
                    token = value
                    break
                if key == "error":
                    error = value
                    break
            print("Acces", token)
                
            userInfo = GoogleGetUserInfo(token)
            
            # sub = request.data.get('sub')#Login Google
            sub = userInfo['sub']
            email = userInfo['email']
            request.data['sub'] = sub
            request.data['email'] = email
            return self.create(request, *args, **kwargs)
        except Exception as e:
            raise BaseException(e)
        # sub = request.data.get('sub')#Login Google
        # username = request.data.get('username')#Login Google
        # email = request.data.get('email')#Login Google
    
    def perform_create(self, serializer):
        serializer.save(is_active = True)

        
class RetrieveUpdateUser(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerialiser
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def perform_update(self, serializer):
        account_type = serializer.validated_data.get('account_type')
        print("UP")
        try:
            group = Group.objects.get(name = f"{account_type}s")
            userInstance = serializer.instance
            print("userInstance", userInstance.groups)
            if not userInstance.groups.all() and not userInstance.groups.filter(name = group.name).exists() :
                print("ADD")
                userInstance.groups.add(group)
                serializer.save()                                

            print("Group", group)
            print("userInstance", userInstance)
        except Exception as e:
            return Response({"message" : f"Groupe {account_type} n'existe pas "}) 