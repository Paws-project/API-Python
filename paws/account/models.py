from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name="Birth Date")
    passport = models.ImageField(verbose_name="Passport")
    verified = models.BooleanField(verbose_name="Verified status")