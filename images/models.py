from django.db import models
import datetime as dt

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    pic_image = models.ImageField(upload_to = 'images/', null=True)