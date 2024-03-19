from django.db import models
#import resize 
from django_resized import ResizedImageField
# import user model 
from django.contrib.auth.models import User

#Adding class for genre 
class Genre(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


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
    isbn_number = models.CharField(max_length=13, null=True, blank=True)
    genre = models.ForeignKey(Genre, null=True, blank=False, on_delete=models.CASCADE)
    language = models.ForeignKey(
        Language, null=True, blank=False, on_delete=models.CASCADE
    )
    description = models.TextField(max_length=300, null=True, blank=False,)
    def __str__(self):
        return self.title