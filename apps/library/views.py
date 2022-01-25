from django.http import Http404
from django.shortcuts import render
from django.views import generic
from apps.library.models import Book


class BookListView(generic.TemplateView):
    """Представоение для получения всех книг"""
    template_name = 'book-list.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['book_list'] = Book.objects.all()
        return context


class BookDetailView(generic.TemplateView):
    """Представление для получения детальной страницы книг"""
    template_name = 'book-detail.html'

    def get_context_data(self, **kwargs):
        context = dict()
        try:
            context['book'] = Book.objects.get(id=kwargs['pk'])
        except Book.DoesNotExist:
            raise Http404
        return context
