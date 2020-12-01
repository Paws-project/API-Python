from rest_framework import authentication
from rest_framework.request import Request

from paws.authentication.models import GoogleAccount

class OAuth2Authentication(authentication.BaseAuthentication):
    def authenticate(self, request: Request):
        if "Authorization" in request.headers:
            auth_header:str = request.headers["Authorization"]
            auth_attributes = auth_header.split(" ")
        else:
            return None
        if len(auth_attributes) != 2:
            return None

        if auth_attributes[0] == "google":
            account = GoogleAccount.objects.get(access_token=auth_attributes[1])
            if account:
                return [account.user, None]
        else:
            return None
