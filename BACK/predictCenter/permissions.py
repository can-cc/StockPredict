from rest_framework import permissions
from rest_framework.compat import (get_model_name, oauth2_provider_scope, oauth2_constants)


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
            )
