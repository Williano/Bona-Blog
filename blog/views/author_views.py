# Core Django imports.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
)

# Blog application imports.
from blog.models.blog_models import Article


class AuthorArticlesListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/author_articles.html'

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=author)

    def get_context_data(self, **kwargs):
        context = super(AuthorArticlesListView, self).get_context_data(**kwargs)
        author = get_object_or_404(User, username=self.kwargs.get('username'))
        context['author'] = author
        return context


class AuthorsListView(ListView):
    model = User
    context_object_name = 'authors'
    template_name = 'blog/authors_list.html'
