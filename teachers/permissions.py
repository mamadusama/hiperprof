from rest_framework.permissions import BasePermission


class TeacherListPernission(BasePermission):
    def has_permission(self, request, view):
        
        return bool(
            request.method not in ("PUT", "DELETE") 
            or request.user 
            and request.user.is_authenticated
        )
        
        
        # essa expressão é equivalente a:
        
        #if request.method not in ['PUT', 'DELETE']:
           # return True
        #return request.user and request.user.is_authenticated
        