from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name="Birth Date")

class GoogleAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    openid = models.CharField(max_length=60, verbose_name="Google OpenID")
    access_token = models.TextField(verbose_name="Acess Token")
    refresh_token = models.TextField(verbose_name="Refresh Token")

class Owner(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    passport = models.ImageField(verbose_name="Passport")
    passport_valid = models.BooleanField(verbose_name="Is passport validated?")


class Shelter(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
