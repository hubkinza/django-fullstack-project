from django.db import models
from cloudinary.models import CloudinaryField

class Events(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
