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




""" View function for adding a new book. """
@login_required
def AddBook(request):
   
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = BookForm(request.POST or None, request.FILES)
        if form.is_valid():
            # If the form data is valid, save the book and associate it with the current user
            form.instance.user = request.user
            form.save()
            # Display a success message and redirect to the books page
            messages.success(request, 'Book successfully added!')
            return redirect('books')
        # If the form data is invalid, display an error message
        messages.error(request, 'An error occurred. Please try again.')
    # If the request method is GET, initialize an empty form
    form = BookForm()
    template = 'books/AddBook.html'
    context = {
        'form': form,
    }
    # Render the AddBook form template with the form
    return render(request, template, context)




"""
    A ListView class for displaying a list of books.
"""
class Books(LoginRequiredMixin, ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "books/books.html"
    context_object_name = 'books'
    
    def get_queryset(self, **kwargs):

        query = self.request.GET.get('q')
        if query:
            # Filter books by title, author, genre, and language containing the search query
            books = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(genre__icontains=query) |
                Q(language__icontains=query)
            )
        else:
            # If no search query provided, return all books
            books = self.model.objects.all()
        return books


class BookDetail(DetailView):
    model = Book
    template_name = "books/book_details.html"
    context_object_name = 'book'


"""View function for Editing book."""
@login_required
def edit_book(request, id):
   
    book = get_object_or_404(Book, id=id)
    
    # Check if the current user is the owner of the book
    if book.user != request.user:
        # If not, display an error message and redirect to the books page
        messages.error(request, 'Access denied. Please try again.')
        return redirect('books')
    
    # If the user matches the book user, proceed with editing
    # Initialize a form for editing the book with data from the request or from the existing book
    form = BookForm(request.POST or None, request.FILES, instance=book)
    
    # Check if the form is submitted via POST method
    if request.method == 'POST':
        # Validate the form
        if form.is_valid():
            # Assign the current user as the owner of the book and save
            form.instance.user = request.user
            form.save()
            # Display a success message and redirect to the books page
            messages.success(request, 'Book successfully updated!')
            return redirect('books')
        # If the form is invalid, display an error message
        messages.error(request, 'An error occurred. Please try again.')
    
    # If the request method is not POST, initialize the form with the existing book data
    form = BookForm(instance=book)
    template = 'books/edit_book.html'
    context = {
        'form': form,
    }
    return render(request, template, context)



"""View function for deleting book."""
@login_required
def delete_book(request, id):
    # Retrieve the book object with the given id from the database
    book = get_object_or_404(Book, id=id)
    
    # Check if the current user is the owner of the book
    if book.user != request.user:
        # If not, display an error message and redirect to the books page
        messages.error(request, 'Access denied. Please try again.')
        return redirect('books')
    
    # If the user matches the book user, proceed with deleting the book
    book.delete()
    
    # Display a success message and redirect to the books page
    messages.success(request, 'Book successfully deleted.')
    return redirect('books')