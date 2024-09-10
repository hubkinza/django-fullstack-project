from django import forms
from .models import Book, WishList

"""Form to Add a new book"""


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "ISBN",
            "image",
            "language",
            "genre",
            "description",

        ]


labels = {
            "title": "Book Title",
            "author": "Author",
            "ISBN": "ISBN",
            "image": "Book Cover",
            "genre": "Genre",
            "language": "Language",
            "descrition": "Brief description of book",

        }
