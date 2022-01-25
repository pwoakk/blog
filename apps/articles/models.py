from django.db import models


class ArticleCategory(models.Model):
    title = models.CharField(max_length=120, unique=True)


class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE, related_name='articles')


class ArticleTag(models.Model):
    name = models.CharField(max_length=50)
    article = models.ManyToManyField(to=Article, related_name='tags')



