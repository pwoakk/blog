from django.db import models


class BookGenre(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    write_year = models.IntegerField()
    genre = models.ForeignKey(to=BookGenre, on_delete=models.CASCADE, related_name='books')
