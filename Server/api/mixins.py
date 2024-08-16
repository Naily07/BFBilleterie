from django.http import Http404
from rest_framework import permissions
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from eventManagement.models import PointDeVenteToEvenement
class OrganisateursEditorMixin():
    permission_classes = [IsAuthenticated, IsOrganisateur]

class PointDeVenteEditorMixin():
    permission_classes =  [IsAuthenticated, IsPointDeVente]

class ClientEditorMixin():
    permission_classes = [IsAuthenticated, IsClients]
    
class OwnerQuerySet(generics.GenericAPIView):
    qs_field = "owner"
    qs_filter_type_event = ''

    def get_queryset(self):
        qs = super().get_queryset()
        owner = self.request.user
        print(owner.groups.all())
        if owner.groups.filter(name="pointdeventes").exists():
            pdvOwner : PointDeVente = PointDeVente.objects.filter(username__iexact = owner).first()
            return Evenement.objects.filter(PDVToEvent_related__pdv=pdvOwner)
        data = {}
        if len(self.qs_filter_type_event)>0:
            data[self.qs_filter_type_event] =  self.kwargs['type_event']
        if owner.groups.filter(name='clients').exists():
            return qs
        data[self.qs_field] = owner
        return qs.filter(**data)


from account.models import CustomUser, PointDeVente
from eventManagement.models import Evenement
class AddTicketQuerySet(generics.GenericAPIView):
    qs_field_event = "slug"

    def get_queryset(self):
        slug = self.kwargs[self.qs_field_event]
        user = self.add_qs_field_user()
        event = Evenement.objects.filter(slug__iexact = slug, owner__exact = user).first()
        print(event)
        qs = super().get_queryset()
        filtre = {'event' : event}
        result = qs.filter(**filtre)

        if not result:
            raise Http404()
        return result

    def add_qs_field_user(self):
        pk = self.kwargs['pdvId']
        pdv = PointDeVente.objects.filter(id__iexact = pk).first()
        if not pdv:
            raise Http404()
        print(pdv.owner)
        return pdv.owner 

class OwnerQuerySetQrCode(generics.GenericAPIView):

    def get_queryset(self):
        qs = super().get_queryset()
        event = Evenement.objects.get(slug = self.kwargs.get('slug'))
        user = self.request.user
        filterData = {'event' : event}
        if user.groups.filter(name = "clients").exists():
            filterData['addOwner'] = user
        print(qs.filter(**filterData))
        
        return qs.filter(**filterData)