from ninja import Router
import time
from django.http import StreamingHttpResponse
import cv2
from asgiref.sync import sync_to_async
from typing import List

from starlette.responses import JSONResponse

from .models import Stream
from api.schemas import StreamSchema

app_router = Router()


@app_router.get("/streams/", response=List[StreamSchema])
def get_streams(request):
    qs = Stream.objects.all()
    return qs


@app_router.get("/streams/{stream_id}")
async def stream_view(request, stream_id: int):
    try:
        stream = await sync_to_async(Stream.objects.get)(id=stream_id)
        return StreamingHttpResponse(await sync_to_async(gen_frames)(stream.rtsp_url),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
    except Stream.DoesNotExist:
        return JSONResponse(content={"error": "Stream not found"}, status_code=404)


def gen_frames(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        time.sleep(0.1)
