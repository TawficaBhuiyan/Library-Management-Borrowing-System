from rest_framework import permissions

class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow if user is admin
        if request.user.is_staff:
            return True
        
        # Allow if the object is the same as the requesting user
        return obj == request.user
