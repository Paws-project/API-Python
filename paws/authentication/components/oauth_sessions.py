from django.conf import settings
import requests
from urllib.parse import urlencode

class OAuthStrategy:
    def __init__(self, client_id:str, client_secret:str, scope:list, redirect_uri:str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.redirect_uri = redirect_uri

    def get_auth_url(self):
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "prompt": "consent",
            "access_type": "offline",
            "response_type": "code",
            "scope": " ".join(self.scope)
        }
        return settings.GOOGLE_AUTH_URI + "?" + urlencode(params)

    def token_exchange(self, code:str):
        data = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "redirect_uri": settings.GOOGLE_REDIRECT_URI
        }
        response = requests.post(settings.GOOGLE_TOKEN_URI, data=data)
        if response.ok:
            return response.json()
        else:
            return {}

    def token_refresh(self, refresh_token):
        pass

    def get_bearer(self, uri, access_token:str):
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(uri, headers=headers)
        if response.ok:
            return response.json()
        else:
            return {}


google = OAuthStrategy(
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    redirect_uri=settings.GOOGLE_REDIRECT_URI,
    scope=settings.GOOGLE_OAUTH_SCOPE,
)
