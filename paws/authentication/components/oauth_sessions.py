from requests_oauthlib import OAuth2Session
from django.conf import settings

google = OAuth2Session(
    client_id=settings.GOOGLE_CLIENT_ID,
    redirect_uri=settings.GOOGLE_REDIRECT_URI,
    scope=settings.GOOGLE_OAUTH_SCOPE,
)