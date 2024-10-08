from django.contrib import admin

# Register your models here.
from .models import Book, WishList


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "image",
        "genre",
        "language",
        "ISBN",

    )
    list_filter = ('title', 'author',)


admin.site.register(WishList)
