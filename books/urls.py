
from . import views
from django.urls import path
from .views import Books ,add_to_wishlist



urlpatterns = [

    path("AddBook/", views.AddBook, name="AddBook"),
    path("books/", views.Books.as_view(), name="books"),
    path("<slug:pk>/", views.BookDetail.as_view(), name="book_details"),
    path("edit/<int:id>/", views.edit_book, name="edit_book"),
    path("delete/<slug:id>/", views.delete_book, name="delete_book"),
    path("add-to-wishlist/<int:id>/", views.add_to_wishlist, name="wishlist"),

  
]
