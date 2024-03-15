from rest_framework import permissions

class IsOrganisateur(permissions.BasePermission):
    
    def has_permission(self, request, view):
        print("permissions", request.user.groups.all())
        if not (request.user.groups.filter(name='organisateurs').exists() |  request.user.is_superuser):
            return False            
        else :
            return super().has_permission(request, view)

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
