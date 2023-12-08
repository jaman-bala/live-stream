import cv2
from asgiref.sync import sync_to_async


async def async_cap_read(cap):
    return await sync_to_async(cap.read)()


async def async_imencode(frame):
    return await sync_to_async(cv2.imencode)('.jpg', frame)


async def gen_frames(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    try:
        while True:
            ret, frame = await async_cap_read(cap)
            if not ret:
                break
            _, buffer = await async_imencode(frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    finally:
        cap.release()

