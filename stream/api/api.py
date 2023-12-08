from typing import List
from django.http import StreamingHttpResponse, HttpResponse
from asgiref.sync import sync_to_async
from ninja import Router
from video.models import IPCamera
from .schemas import StreamSchema
from video.views import gen_frames

stream_router = Router()


@stream_router.get("/streams/", response=List[StreamSchema])
async def get_streams_all(request):
    qs = await sync_to_async(list)(IPCamera.objects.all())
    return qs


@stream_router.get("/streams/{stream_id}")
async def stream_streams_id(request, stream_id: int):
    try:
        stream = await sync_to_async (IPCamera.objects.get)(id=stream_id)
        return StreamingHttpResponse(gen_frames(stream.rtsp_url),
                                  content_type='multipart/x-mixed-replace; boundary=frame')
    except IPCamera.DoesNotExist:
        return HttpResponse(content={"error": "Stream not found"}, status_code=404)

