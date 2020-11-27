from django.contrib import admin

from paws.authentication.models import GoogleAccount
# Register your models here.

@admin.register(GoogleAccount)
class AdminGoogleAccount(admin.ModelAdmin):
    pass
