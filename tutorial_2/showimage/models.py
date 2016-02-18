from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.

class ShowImage(models.Model):
    image_name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to="")