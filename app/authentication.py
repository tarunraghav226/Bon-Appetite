from django.contrib.auth.models import User
from rest_framework import authentication, exceptions

from helpers import jwt_authentication_helper


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = jwt_authentication_helper.get_username_from_jwt(request)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User Not Found")

        return (user, None)
