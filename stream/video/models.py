from django.db import models


class Stream(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    rtsp_url = models.CharField(max_length=200)
