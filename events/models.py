from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField

class Events(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
