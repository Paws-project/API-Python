from django.views import View
from django.http import HttpRequest, JsonResponse
from django.conf import settings
from django.shortcuts import redirect, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.views import APIView, Response, Request


from paws.authentication.models import GoogleAccount
from paws.authentication.serializers import UserSerializer
from paws.authentication.components.oauth_sessions import google

from pprint import pprint
from requests import get
from urllib.parse import urlencode
class AuthView(View):
    def get(self, request: HttpRequest):
        url = google.get_auth_url()
        return redirect(url)

class AuthCallbackView(View):
    def get(self, request: HttpRequest):
        try:
            # print(request.headers)
            code = request.GET["code"]
        except KeyError as err:
            print(err)
            return JsonResponse({"message": f"Missing parameter(s)"}, status=422)

        tokens = google.token_exchange(code)
        pprint(tokens)
        print("--------------------------------------------------")
        userdata = google.get_bearer(settings.GOOGLE_USERINFO_URI, tokens["access_token"])
        pprint(userdata)
        user = User(
            username=userdata["email"],
            email=userdata["email"],
            first_name=userdata.get("given_name", ""),
            last_name=userdata.get("family_name", "")
        )
        account = GoogleAccount(
            user=user,
            openid=userdata.get("id", ""),
            access_token=tokens["access_token"],
            refresh_token=tokens["refresh_token"]
        )
        try:
            user.set_unusable_password()
            user.full_clean()
            account.full_clean(exclude=["user"])
        except ValidationError as err:
            print(err)
            return JsonResponse({"messages": f", ".join(err.messages)}, status=409)

        user.save()
        account.save()
        # TODO: Fix redirect to deep link
        resp = HttpResponse("", status=302)
        resp["Location"] = "paws://googleauth?" + urlencode({"user": user.pk, "access_token": tokens["access_token"]})
        resp["Location"] = "http://api.pawsproject.com?" + urlencode({"user": user.pk, "access_token": tokens["access_token"]})
        print(resp)
        return resp


class UserView(APIView):
    def get(self, request: Request, pk:int=0) -> Response:
        user = User.objects.get(pk=pk)
        return Response(UserSerializer(user).data)
