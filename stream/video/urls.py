from django.urls import path
from video.views import stream_view

urlpatterns = [
    path('streams/<int:stream_id>', stream_view, name='video_stream'),
]