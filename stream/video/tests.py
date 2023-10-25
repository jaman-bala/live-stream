from django.test import TestCase

# Create your tests here.
# import cv2
# from django.shortcuts import render
# from django.http import StreamingHttpResponse
# from .models import Stream
#
#
# def gen_frames(rtsp_url):
#     print(cv2.getBuildInformation())
#     cap = cv2.VideoCapture(rtsp_url)
#
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#
#         (flag, encodedImage) = cv2.imencode(".jpg", frame)
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
#
#
# def stream_view(request, stream_id):
#     stream = Stream.objects.get(id=stream_id)
#     return StreamingHttpResponse(gen_frames(stream.rtsp_url), content_type='multipart/x-mixed-replace; boundary=frame')
#
#
# def home_view(request):
#     streams = Stream.objects.all()
#     return render(request, 'home.html', {'streams': streams})