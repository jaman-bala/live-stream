import asyncio
import httpx
import cv2
from ninja import Router
from django.http import StreamingHttpResponse
from asgiref.sync import sync_to_async
from typing import List
from starlette.responses import JSONResponse

from .models import Stream
from api.schemas import StreamSchema

app_router = Router()
cv2.ocl.setUseOpenCL(True)


@app_router.get("/streams/", response=List[StreamSchema])
async def get_streams(request):
    qs = await sync_to_async(list)(Stream.objects.all())
    return qs


async def async_cap_read(cap):
    return await sync_to_async(cap.read)()


async def async_imencode(frame):
    return await sync_to_async(cv2.imencode)('.jpg', frame)


async def gen_frames(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)
    while True:
        ret, frame = await async_cap_read(cap)
        if not ret:
            break
        _, buffer = await async_imencode(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        await asyncio.sleep(0.01)


@app_router.get("/streams/{stream_id}")
async def stream_view(request, stream_id: int):
    try:
        stream = await sync_to_async(Stream.objects.get)(id=stream_id)
        return StreamingHttpResponse(await sync_to_async(gen_frames)(stream.rtsp_url),
                                     content_type='multipart/x-mixed-replace; boundary=frame')
    except Stream.DoesNotExist:
        return JSONResponse(content={"error": "Stream not found"}, status_code=404)
