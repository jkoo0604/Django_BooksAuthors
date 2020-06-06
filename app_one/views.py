from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    return render(request,'index.html')

def books(request):
    # Books template with all books
    context = {
        'all_books': Book.objects.all()
    }
    return render(request,'books.html',context)

def authors(request):
    # Authors template with all authors
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request,'authors.html',context)

def addBook(request):
    # Add a book to the database
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/books')

def addAuthor(request):
    # Add an author to the database
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/authors')

def bookdetail(request, bookid):
    # Display info about a book
    # create key/value for authors excluding one already associated with the book (for drop down)
    bookdetail1 = Book.objects.get(id=bookid)
    authorlist = Author.objects.exclude(id__in=bookdetail1.authors.values_list('id', flat=True))
    context = {
        'bookdetail': bookdetail1,
        'other_authors': authorlist.all(),
    }
    return render(request,'bookdetail.html',context)

def authordetail(request, authorid):
    # Display info about an author
    authordetail1 = Author.objects.get(id=authorid)
    booklist = Book.objects.exclude(id__in=authordetail1.books.values_list('id', flat=True))
    context = {
        'authordetail': authordetail1,
        'other_books': booklist.all(),
    }
    return render(request,'authordetail.html',context)

def addAuthortoBook(request, bookid):
    # On book detail page, add an author in DB to the book
    # Grab author ID from form
    currentauthor = Author.objects.get(id=request.POST['addauthortobook'])
    currentbook = Book.objects.get(id=bookid)
    currentbook.authors.add(currentauthor)

    return redirect('/books')

def addBooktoAuthor(request, authorid):
    # On author detail page, add a book in DB to the author
    currentbook = Book.objects.get(id=request.POST['addbooktoauthor'])
    currentauthor = Author.objects.get(id=authorid)
    currentauthor.books.add(currentbook)

    return redirect('/authors')
