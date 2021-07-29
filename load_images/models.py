from django.db import models

# Create your models here.

class ImageDetail(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField()