from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # logic to show books
    return render(request, "bookshelf/book_list.html")

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # logic to create a book
    return render(request, "bookshelf/book_form.html")

# Create your views here.
