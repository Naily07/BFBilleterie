from rest_framework import permissions
from .permissions import IsOrganisateur
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework import generics
class OgranisateursEditorMixin():
    permission_classes = [IsAuthenticated, IsOrganisateur]

class UserQuerySet(generics.GenericAPIView):
    qs_field = "owner"

    def get_queryset(self):
        qs = super().get_queryset()
        owner = self.request.user
        data = {}
        data[self.qs_field] = owner
        return qs.filter(**data)
