from rest_framework import serializers
from paws.pets.models import Pet, PetPhoto, LostPet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class PetPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetPhoto
        fields = '__all__'

class LostPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPet
        fields = '__all__'
