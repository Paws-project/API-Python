from django.contrib import admin
from paws.pets.models import Pet
# Register your models here.
@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    pass