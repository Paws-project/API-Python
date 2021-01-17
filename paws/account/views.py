from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.views import APIView, Response, Request

import jwt
from datetime import datetime, timedelta


class Login(APIView):
    """
    View for obtaining a token by login and password
    """

    authentication_classes = []
    permission_classes = []

    def post(self, request: Request):
        username = request.data.get("username", False)
        password = request.data.get("password", False)

        try:
            assert(username and password)
        except AssertionError:
            return Response("Missing parameter (username, password)", status=422)

        user = User.objects.get(username=username)
        if user.check_password(password):
            payload = {
                "usr": user.pk,
                "iat": int(datetime.utcnow().timestamp()),
                "exp": int((datetime.utcnow() + timedelta(minutes=15)).timestamp()),
            }
            token = jwt.encode(payload, settings.SECRET_KEY,
                               settings.JWT_HASH_ALGORITHM)
            return Response(token)

        return Response("Authentication failed", status=402)


class Register(APIView):
    def post(self, request):
        username = request.data.get("username", False)
        password = request.data.get("password", False)
        print(request.user)
        print(request.auth)
        return Response("test")
