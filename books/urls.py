
from . import views
from django.urls import path
from .views import Books


urlpatterns = [

    path("AddBook/", views.AddBook, name="AddBook"),
    path("books/", views.Books.as_view(), name="books"),
     path("<slug:pk>/", views.BookDetail.as_view(), name="book_detail"),
]

