from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from paws.authentication.serializers import UserSerializer
from rest_framework.views import APIView, Response, Request

from paws.authentication.components.oauth_sessions import google

import json
class AuthView(View):
    def get(self, request: Request):
        url = google.authorization_url(settings.GOOGLE_AUTH_URI)[0]
        return redirect(url)

class AuthCallbackView(View):
    def get(self, request: Request):
        try:
            code = request.GET.get("code")
        except KeyError as err:
            print(err)
            return Response(json.dumps({"message": "Missing parameter(s)"}), status=422)

        fetched = google.fetch_token(
            settings.GOOGLE_TOKEN_URI,
            code=code,
            client_secret=settings.GOOGLE_CLIENT_SECRET
        )
        print(fetched)
        return HttpResponse("success")


class UserView(APIView):
    def get(self, request: Request, pk:int=0) -> Response:
        print(pk)
        user = User.objects.all()
        return Response(UserSerializer(user, many=True).data)