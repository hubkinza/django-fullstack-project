#using class based views instead of function based views 
from django.views.generic import TemplateView
#from books.models import Book


class Index(TemplateView):
    template_name = 'events/index.html'
   # model = Book
    #context_object_name = 'books'
