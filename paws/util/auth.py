from rest_framework import authentication
from django.conf import settings
from jwt import decode, ExpiredSignatureError
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class JWTokenAuthentication(authentication.BaseAuthentication):
    """
    Authentication via JSON Web Token
    """

    def authenticate(self, request):
        token = request.headers.get("Authentication")
        try:
            payload = decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.JWT_HASH_ALGORITHM],
                leeway = 120,
                options={
                    "require": ["usr", "iat", "exp"]
                }
            )
        except ExpiredSignatureError as e:
            raise AuthenticationFailed("Token expired")
        except:
            raise AuthenticationFailed("Token validation failed")

        user = User.objects.get(pk=usr)
        return (user, payload)
