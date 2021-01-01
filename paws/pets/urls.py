from django.urls import path, include
from rest_framework import routers

from paws.pets.viewsets import PetViewSet
router = routers.DefaultRouter()

router.register(r"", PetViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls