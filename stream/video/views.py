import cv2
import asyncio
from asgiref.sync import sync_to_async
from django.shortcuts import render
from django.http import StreamingHttpResponse
from .models import Stream


def gen_frames(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')


def stream_view(request, stream_id):
    stream = Stream.objects.get(id=stream_id)
    response = StreamingHttpResponse(gen_frames(stream.rtsp_url),
                                     content_type='multipart/x-mixed-replace; boundary=frame')
    return response


def home_view(request):
    streams = Stream.objects.all()
    return render(request, 'home.html', {'streams': streams})
