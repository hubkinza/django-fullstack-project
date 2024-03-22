from django.db import models
# import resize 
from django_resized import ResizedImageField
# import user model 
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from django.conf import settings 


# A model to create and manage books
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False) 
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="books/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    ISBN = models.CharField(max_length=13, null=True, blank=True)
    genre = models.CharField(max_length=300, null=True, blank=False)
    language = models.CharField(max_length=300, null=True, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=False,)





def __str__(self):
    return self.title
