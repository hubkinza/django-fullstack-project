
from django.urls import path
# import the view from this directory and access the class "index"
from .views import Index


urlpatterns = [
    path('', Index.as_view(), name='home')
]
