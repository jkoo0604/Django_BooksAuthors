from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index),
    path('books/<int:bookid>/addauthortobook', views.addAuthortoBook),
    path('authors/<int:authorid>/addbooktoauthor', views.addBooktoAuthor),
    path('books/<int:bookid>', views.bookdetail),
    path('authors/<int:authorid>', views.authordetail),
    path('books', views.books),
    path('authors', views.authors),
    path('addbook', views.addBook),
    path('addauthor', views.addAuthor),
    
]