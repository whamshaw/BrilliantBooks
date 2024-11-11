from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover = models.ImageField(upload_to='covers/')
    language = models.CharField(max_length=50)
    ranking = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class ReadingList(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    read_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} - {'Read' if self.read_status else 'Unread'}"
