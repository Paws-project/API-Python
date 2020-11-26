from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    google_id = models.IntegerField(verbose_name="Google OpenID")
    birth_date = models.DateField(verbose_name="Birth Date")

class Owner(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    passport = models.ImageField(verbose_name="Passport")
    passport_valid = models.BooleanField(verbose_name="Is passport validated?")


class Shelter(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
