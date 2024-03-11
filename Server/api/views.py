from django.shortcuts import render
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.tokens import Token
from rest_framework.views import APIView
from api.utils import decodeToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import jwt
from rest_framework_simplejwt.settings import api_settings
# Create your views here.

from account.views import RegisterPDV
from account.models import PointDeVente
from account.serializer import PointDeVenteSerializer
from rest_framework.generics import ListCreateAPIView
from account.models import MyUser
class TokenActivateView(ListCreateAPIView):
    queryset = PointDeVente.objects.all()
    serializer_class = PointDeVenteSerializer

    def perform_create(self, serializer):
        try :
            owner_id = self.request.data.get('user_id')
            owner = MyUser.objects.filter(id__iexact = owner_id).first()
            username = serializer.validated_data.get('username')
            print("NAME", username)
            if owner and username :
                print("IDD", owner)
                serializer.save(owner = owner, username = username)
            return Response({"Error" : "Not Save"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            raise BaseException(e)

    def get(self, request):
        token = (request.query_params.get('token'))
        print("get", token)
        try:
            # mytoken = TokenVerifyView.
            decoded_token = jwt.decode(token, api_settings.SIGNING_KEY, algorithms=[api_settings.ALGORITHM])
            print("isVerifier", decoded_token)
            result = RegisterPDV.create(self, request, decoded_token)
            print("Result", result)
            if (result.status_code == 200) | (result.status_code == 201):
                return RegisterPDV.get(self, request)
            return result
        except Exception as e:
            print("Error", e)        
            return Response({"error" : f"createPDV {e}"})


from eventManagement.models import *
def creatPointDeVente(self, request, data, *args):
    print("DATAS", *args)
    datas = args[0]
    for key, value in datas.items():
        if key == "list_event":
            list_event = value
        print(value) 
    nom_pdv = ""

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
    serializer.save(owner = self.request.user, is_active = False)