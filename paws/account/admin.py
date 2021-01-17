from django.contrib import admin
from paws.account.models import Profile

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass