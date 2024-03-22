#using class based views instead of function based views 
from django.views.generic import ListView
from books.models import Book


class Index(ListView):
    template_name = 'events/index.html'
    model = Book
    context_object_name = 'books'

def get_queryset(self):
    return self.model.objects.all()[:3]
