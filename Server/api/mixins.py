from django.http import Http404
from rest_framework import permissions
from .permissions import IsOrganisateur, IsPointDeVente
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
class OrganisateursEditorMixin():
    permission_classes = [IsAuthenticated, IsOrganisateur]

class PointDeVenteEditorMixin():
    permission_classes =  [IsAuthenticated, IsPointDeVente]

class UserQuerySet(generics.GenericAPIView):
    qs_field = "owner"

    def get_queryset(self):
        qs = super().get_queryset()
        owner = self.request.user
        data = {}
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