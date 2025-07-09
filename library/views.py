from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import BookForm

def home(request):
    return render(request, 'library/home.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    if query:
        books = books.filter(isbn__icontains=query) | books.filter(category__name__icontains=query)
    return render(request, 'library/book_list.html', {'books': books})
