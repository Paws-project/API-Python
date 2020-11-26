from rest_framework import serializers
from django.contrib.auth.models import User
from paws.authentication.models import Owner

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["url", "profile", "passport", "passport_valid"]