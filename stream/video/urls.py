from django.urls import path
from stream.api.api import stream_streams_id

urlpatterns = [
    path('streams/<int:stream_id>', stream_streams_id, name='video_stream'),
]