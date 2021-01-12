from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from paws.pets.models import Pet, LostPet
from paws.pets.serializers import PetSerializer, PetPhotoSerializer, LostPetSerializer

from paws.authentication.classes import OAuth2Authentication

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetPhotoViewSet(viewsets.ModelViewSet):
    # queryset = Pet.objects.filter("check for user")
    queryset = Pet.objects.all()
    serializer_class = PetPhotoSerializer

class LostPetViewSet(viewsets.ModelViewSet):
    queryset = LostPet.objects.all()
    serializer_class = LostPetSerializer
