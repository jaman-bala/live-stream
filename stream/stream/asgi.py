import os

from django.core.asgi import get_asgi_application
from django.conf import settings
from uvicorn.workers import UvicornWorker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stream.settings')

application = get_asgi_application()

# Добавьте следующие строки для асинхронного запуска через uvicorn
if settings.DEBUG:
    from channels.layers import get_channel_layer
    channel_layer = get_channel_layer()
    import django

    django.setup()


def get_asgi_application():
    return application
