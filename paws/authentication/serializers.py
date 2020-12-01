from rest_framework import serializers
from django.contrib.auth.models import User
from paws.authentication.models import Owner, GoogleAccount

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

class GoogleAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleAccount
        exclude = ["user"]

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["profile", "passport", "passport_valid"]