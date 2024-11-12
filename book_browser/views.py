from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.db.models import Q
from .models import Book, ReadingList, UserProfile, Author, Genre

@login_required
def index(request):
    # Fetch recommendations
    recommendations = Book.objects.order_by('-rating')[:5]

    user = request.user

    # Get the user_profile
    user_profile = UserProfile.objects.get(user=user)

    # Fetch reading list using the user_profile
    reading_list = ReadingList.objects.filter(user_profile=user_profile)

    # Create a set of book IDs in the reading list for quick lookup
    reading_list_book_ids = set(reading_list.values_list('book_id', flat=True))

    context = {
        'recommendations': recommendations,
        'reading_list': reading_list,
        'reading_list_book_ids': reading_list_book_ids,
    }

    return render(request, 'index.html', context)

@login_required
def search_results(request):
    query = request.GET.get('q')
    if query:
        search_results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )
    else:
        search_results = None

    context = {
        'search_results': search_results,
    }

    return render(request, 'search_results.html', context)

@login_required
def browse(request, sort_by):
    if sort_by == 'popularity':
        books = Book.objects.order_by('-rating')
        context = {
            'sort_by': sort_by,
            'books': books,
        }
    elif sort_by == 'author':
        authors = Author.objects.prefetch_related('books').all()
        context = {
            'sort_by': sort_by,
            'authors': authors,
        }
    elif sort_by == 'genre':
        genres = Genre.objects.prefetch_related('books').all()
        context = {
            'sort_by': sort_by,
            'genres': genres,
        }
    else:
        books = Book.objects.all()
        context = {
            'sort_by': 'all',
            'books': books,
        }

    return render(request, 'browse.html', context)

@login_required
def add_to_reading_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    reading_list, created = ReadingList.objects.get_or_create(user_profile=user_profile, book=book)
    return redirect('index')

@login_required
def remove_from_reading_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_profile = UserProfile.objects.get(user=request.user)
    ReadingList.objects.filter(user_profile=user_profile, book=book).delete()
    return redirect('index')