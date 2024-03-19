from django.db import models
#import resize 
from django_resized import ResizedImageField
# import user model 
from django.contrib.auth.models import User


# A model to create and manage books
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.title