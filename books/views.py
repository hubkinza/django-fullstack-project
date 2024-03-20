
from django.views.generic import CreateView
from .models import Book
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AddBook(LoginRequiredMixin, CreateView):
    """Add a new book"""
    template_name = "books/addbook.html"
    model = Book
    form_class= BookForm
    Success_url = '/books/'

def form_valid(self, form):
    form.instance.user = self.request.user
    return super(AddBook, self).form_valid(form)   

