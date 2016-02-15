from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_description = models.CharField(max_length=500)
    store_image = models.FileField(default='')
    store_creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.store_name

