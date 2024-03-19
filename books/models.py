from django.db import models
#import resize 
from django_resized import ResizedImageField

#A model to create and manage books
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
    genre = models.ForeignKey(Genre, null=False, blank=False, on_delete=models.CASCADE)
    language = models.ForeignKey(
        Language, null=False, blank=False, on_delete=models.CASCADE
    )
    description = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.title