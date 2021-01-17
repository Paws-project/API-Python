from django.contrib import admin
from paws.pets.models import Pet

@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    pass