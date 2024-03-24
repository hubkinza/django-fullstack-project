from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Book
from .forms import BookForm
from .models import WishList
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
# handle message and redirect error
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q

@login_required
@permission_required('books.AddBook', raise_exception=True)
def AddBook(request):

    """ View function for adding a new book. """

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


@login_required
def edit_book(request, id):
    """View function for Editing book."""
    book = get_object_or_404(Book, id=id)

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

@login_required
def delete_book(request, id):

    """View function for deleting book."""
    # Retrieve the book object with the given id from the database
    book = get_object_or_404(Book, id=id)
    book.delete()
    # Display a success message and redirect to the books page
    messages.success(request, 'Book successfully deleted.')
    return redirect('books')



@login_required
def add_to_wishlist(request, id):
 
    """View function for Adding book to wishlist."""   
    book = get_object_or_404(Book, id=id)

    # if request.user.wishlist.filter(book=book).exists():
    if WishList.objects.filter(user=request.user, book=book).exists():  
     messages.info(request, 'This book is already in your wish list.')
     return redirect('books')

    # Create a new wish list entry for the current user and the selected book
    wishlist_entry = WishList(user=request.user, book=book)
    wishlist_entry.save()

    # Display a success message and redirect
    messages.success(request, 'Book added to your wish list.')
    # return redirect('books', pk=id)
    return redirect('books')


@login_required
def delete_from_wishlist(request, id):

    wishlist_entry = WishList(user=request.user, book=book)
    wishlist_entry.delete()
    return redirect('books')

@login_required
def delete_from_wishlist(request, id):
    """View function for deleting an item from the wishlist."""
    # Retrieve the wishlist entry with the given id from the database
    wishlist_entry = get_object_or_404(WishlistEntry, id=id)

    # Delete the wishlist entry
    wishlist_entry.delete()

    # Display a success message and redirect to the wishlist page
    messages.success(request, 'Item successfully deleted from wishlist.')
    return redirect('wishlist')



@login_required
def wishlist_page(request):
    # Retrieve the current user's wishlist items
    wishlist = WishList.objects.filter(user=request.user)
    print(f'wishlist: {wishlist}')
    return render(request, 'books/wishlist.html', {'list': wishlist})