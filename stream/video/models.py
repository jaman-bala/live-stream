from django.db import models


class IPCamera(models.Model):
    title = models.CharField(max_length=255)
    rtsp_url = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'
