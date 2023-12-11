import cv2
import os
import time
from asgiref.sync import sync_to_async
from setuptools.sandbox import save_path

save_path = 'static/cameras'

def gen_frames(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)
    cap.set(cv2.CAP_PROP_FPS, 2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 2, (640, 480))
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            _, buffer = cv2.imencode('.jpg', frame)
            img_filename = f'frame_{time.time()}.jpg'
            img_path = os.path.join(save_path, img_filename)
            cv2.imwrite(img_path, frame)
            out.write(frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    finally:
        cap.release()





# Асинъронная версия
# import cv2
# from asgiref.sync import sync_to_async
#
#
# async def async_cap_read(cap):
#     return await sync_to_async(cap.read)()
#
#
# async def async_imencode(frame):
#     return await sync_to_async(cv2.imencode)('.jpg', frame)
#
#
# async def gen_frames(rtsp_url):
#     cap = cv2.VideoCapture(rtsp_url)
#     cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
#     try:
#         while True:
#             ret, frame = await async_cap_read(cap)
#             if not ret:
#                 break
#             _, buffer = await async_imencode(frame)
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
#     finally:
#         cap.release()