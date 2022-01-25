from django.contrib import admin
from .models import Book, BookGenre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    pass


