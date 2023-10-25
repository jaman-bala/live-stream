from django.urls import path
from .views import stream_view, home_view

urlpatterns = [
    path('', home_view, name='stream'),
    path('stream/<int:stream_id>/', stream_view, name='stream'),
]

