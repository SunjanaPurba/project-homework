from django.shortcuts import render, redirect, get_object_or_404
from ..models import Book
from app_F.models import Book

def book_list(request):

    books = Book.objects.all()
    context = {
        'books': books,
        'message' : 'This is FBVS'
    }
    return render(request, 'books/book_list.html', context)

def book_add(request):
    if request.method == 'POST':
        new_book = Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            published_date=request.POST.get('published_date')
        )
        return redirect('book_list')
    return render(request, 'books/book_form.html')

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk) 
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk) 
    if request.method == 'POST':
        book.delete() 
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book}) 

