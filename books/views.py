from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Book
from .forms import BookForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
#handle message and redirect error 
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse



@login_required
def AddBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Book successfully added!')
            return redirect('books')
        messages.error(request, 'An error occurred. Please try again.')
    form = BookForm()
    template = 'books/AddBook.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


class Books(LoginRequiredMixin, ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "books/books.html"
    context_object_name = 'books'
    
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            books = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(genre__icontains=query) |
                Q(language__icontains=query)
            )
        else:
            books = self.model.objects.all()
        return books


class BookDetail(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = 'book'

