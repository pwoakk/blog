from django.http import Http404
from django.shortcuts import render
from django.views import generic
from apps.articles.models import Article


class ArticleListView(generic.TemplateView):
    """Представоение для получения всех публикаций"""
    template_name = 'article-list.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['article_list'] = Article.objects.all()
        return context


class ArticleDetailView(generic.TemplateView):
    """Представление для получения детальной страницы публикации"""
    template_name = 'article-detail.html'

    def get_context_data(self, **kwargs):
        context = dict()
        try:
            context['article'] = Article.objects.get(id=kwargs['pk'])
        except Article.DoesNotExist:
            raise Http404
        return context
