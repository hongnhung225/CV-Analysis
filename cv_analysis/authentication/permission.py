from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class IsHR(BasePermission):
    def has_permission(self, request, view):
        try:
            user = JWTAuthentication().authenticate(request)[0]
            if user.role == 'hr':
                return True
            else:
                return False
        except AuthenticationFailed as ex:
            return False

class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        try:
            user = JWTAuthentication().authenticate(request)[0]
            if user.role == 'cand':
                return True
            else:
                return False
        except AuthenticationFailed as ex:
            return False