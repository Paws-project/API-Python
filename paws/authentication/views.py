from django.views import View
from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, HttpResponse 
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.views import APIView, Response, Request


from paws.authentication.models import GoogleAccount
from paws.authentication.serializers import UserSerializer, GoogleAccountSerializer
from paws.authentication.components.oauth_sessions import google


from urllib.parse import urlencode
class AuthView(View):
    def get(self, request: HttpRequest):
        url = google.get_auth_url()
        return redirect(url)

class AuthCallbackView(View):
    def get(self, request: HttpRequest):
        try:
            code = request.GET["code"]
        except KeyError as err:
            return JsonResponse({"message": f"Missing parameter(s): {err}"}, status=422)
# TODO: Create classes for tokens and userdata
        tokens = google.token_exchange(code)
        userdata = google.get_bearer(settings.GOOGLE_USERINFO_URI, tokens["access_token"])

# TODO: User signing in
        user = UserSerializer(
            data = {
                "username": userdata["email"],
                "email": userdata["email"],
                "first_name": userdata.get("given_name", ""),
                "last_name": userdata.get("family_name", "")
            }
        )
        account = GoogleAccountSerializer(
            data = {
                "openid": userdata["id"],
                "access_token": tokens["access_token"],
                "refresh_token": tokens["refresh_token"]
            }
        )


        if user.is_valid() and account.is_valid():
            # Link and save models
            user = user.save()
            GoogleAccount(user=user, **account.validated_data).save()

            response = HttpResponse("", status=302)
            redirect_uri = f"{settings.GOOGLE_CUSTOM_LINK}?{urlencode({'user': user.pk, 'access_token': tokens['access_token']})}"
            response["Location"] = redirect_uri
            del response["X-Frame-Options"]
            del response["X-Content-Type-Options"]
            return response
        else:
            return JsonResponse({"message": "Data is invalid"}, status=409)
            # return JsonResponse({
            #     "messages": f", ".join(err.messages),
            # }, status=409)


class UserView(APIView):
    def get(self, request: Request, pk:int=0) -> Response:
        user = User.objects.get(pk=pk)
        return Response(UserSerializer(user).data)        
    