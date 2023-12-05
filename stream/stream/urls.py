from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from video.views import app_router

api = NinjaAPI()
api.add_router("/", app_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),
]