from django.db import models


class Stream(models.Model):
    title = models.CharField(max_length=255)
    rtsp_url = models.CharField(max_length=200)
