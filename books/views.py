
from django.views.generic import CreateView

from .models import Book
from .forms import BookForm


class AddBook(CreateView):
    """Add a new book"""

    template_name = "books/addbook.html"
    model = Book
    Success_url = '/books/'

def form_valid(self, form):
    form.instance.user = self.request.user
    return super(Addbook, self).form_valid(form)   