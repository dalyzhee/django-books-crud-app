from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import BookForm

def book_list(request):
    book = Books.objects.all()
    data = {}

    data['object_list'] = book
    return render(request, 'books/book_list.html', data)

def book_view(request, pk):
    book = get_object_or_404(Books, pk=pk)
    return render(request, 'books/book_view.html', {'object':book})

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_create.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_create.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_delete.html', {'object': book})
