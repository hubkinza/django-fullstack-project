
from . import views
from django.urls import path
from .views import Books


urlpatterns = [

    path("AddBook/", views.AddBook, name="AddBook"),
    path("books/", views.Books.as_view(), name="books"),
    path("<slug:pk>/", views.BookDetail.as_view(), name="book_details"),
    path("edit/<int:id>/", views.edit_book, name="edit_book"),
      path("delete/<slug:id>/", views.delete_book, name="delete_book"),
]

