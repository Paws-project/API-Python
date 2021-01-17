from django.contrib import admin
from django.urls import path, include
from paws.account.views import Register, Login

urlpatterns = [
    path("login/", Login.as_view()),
    path("register/", Register.as_view()),

    path("auth/", include("paws.authentication.urls")),
    path("pets/", include("paws.pets.urls")),
    path('admin/', admin.site.urls),
]
