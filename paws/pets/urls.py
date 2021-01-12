from django.urls import path, include
from rest_framework import routers

from paws.pets.viewsets import PetViewSet, LostPetViewSet
router = routers.DefaultRouter()

router.register(r"list", PetViewSet)
router.register(r"lost", LostPetViewSet)


urlpatterns = []

urlpatterns += router.urls