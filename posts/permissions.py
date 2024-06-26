from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAuthenticated

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        
        if not request.user.is_authenticated:
            raise NotAuthenticated("User not authenticated.")
        
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the owner of the object or superuser.
        try:
            user_profile = request.user.user_profile
            return obj.author == user_profile or request.user.is_superuser
        except AttributeError:
            # Handle the case where the user does not have a profile
            return request.user.is_superuser
