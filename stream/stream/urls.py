from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from api.api import stream_router

api = NinjaAPI()
api.add_router("/", stream_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),
]