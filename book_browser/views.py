from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Book


def index(request):
    return HttpResponse("Hello, world. You're at the books index.")

def browse_by_popularity(request):
    popular_books = Book.objects.order_by('-ranking')
    template = loader.get_template('browse.html')
    context = {
        'books': popular_books,
    }

    return HttpResponse(template.render(context, request))
