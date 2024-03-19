from django import forms
from .models import Book

"""Form to Add a new book"""
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "image",
            "language",
            "genre",
            "description",
        ]
labels = {
            "title": "Book Title",
            "author": "Author",
            "image": "Book Cover",
            "genre": "Genre",
            "language": "Language",
            "descrition": "Brief description of book",
        }

def save(self, commit=True):
        instance = super(BookForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance

       