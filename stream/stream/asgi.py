import os

from django.core.asgi import get_asgi_application
from django.conf import settings
from uvicorn.workers import UvicornWorker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stream.settings')

application = get_asgi_application()

