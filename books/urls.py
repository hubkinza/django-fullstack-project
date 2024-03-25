
from . import views
from django.urls import path
from .views import Books


urlpatterns = [
    path(
        "AddBook/",
        views.AddBook,
        name="AddBook"),
    path(
        "books/",
        views.Books.as_view(),
        name="books"),
    path(
        "book_detail/<slug:pk>/",
        views.BookDetail.as_view(),
        name="book_details"),
    path(
        "edit/<int:id>/",
        views.edit_book,
        name="edit_book"),
    path(
        "delete/<slug:id>/",
        views.delete_book,
        name="delete_book"),
    path(
        "add_to_wishlist/<int:id>/",
        views.add_to_wishlist,
        name="add_to_wishlist"),
    path(
        "wishlist_page/",
        views.wishlist_page,
        name='wishlist_page'),
    path(
        "delete_from_wishlist/<int:id>",
        views.delete_from_wishlist,
        name="delete_from_wishlist"),
]
