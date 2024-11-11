from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Book

@login_required 
def index(request):
    return HttpResponse("Hello, world. You're at the books index.")

def browse(request, sort_by):
    if sort_by == 'popularity':
        books = Book.objects.order_by('-ranking')
    elif sort_by == 'author':
        books = Book.objects.order_by('author__name')
    elif sort_by == 'genre':
        books = Book.objects.order_by('genre')
    else:
        books = Book.objects.all()

    template = loader.get_template('browse.html')
    context = {
        'books': books,
    }

    return HttpResponse(template.render(context, request))
