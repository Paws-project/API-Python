from django.urls import path
from paws.authentication.views import AuthView, AuthCallbackView, UserView
urlpatterns = [
    path("auth/google", AuthView.as_view()),
    path("auth/google/callback/", AuthCallbackView.as_view()),
    path("model/user/<pk>/", UserView.as_view())
]