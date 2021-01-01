from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from paws.pets.models import Pet
from paws.pets.serializers import PetSerializer

from paws.authentication.classes import OAuth2Authentication

class PetViewSet(viewsets.ModelViewSet):
    # authentication_classes = [ OAuth2Authentication ]
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
