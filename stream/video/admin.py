from django.contrib import admin
from .models import IPCamera


@admin.register(IPCamera)
class IPCamera(admin.ModelAdmin):
    list_display = ('id', 'title')