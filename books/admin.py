from django.contrib import admin

# Register your models here.
from .models import Book,Genre,Language

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "image",
        "genre",
        "language",   
       
    )
    list_filter = ('title', 'author',)
        