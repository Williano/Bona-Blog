# Core Django imports.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView

# Blog application imports.
from blog.models.blog_models import Category, Article, Comment


class ArticleListView(ListView):
    """
     This view list all articles and categories.
    """
    context_object_name = "articles"
    queryset = Article.objects.filter(status='PUBLISHED')
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        """
        Calls the base implementation first to get a context

        :return: dictionary: a dictionary of all categories and their ids
        """
        context = super().get_context_data(**kwargs)
        # Get all blog categories and return it to the view.
        context['categories'] = Category.objects.all()
        return context


class CategoryArticleListView(ListView):
    """
     This view list all articles in a specific category.
    """
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/category_articles.html'

    def get_queryset(self):
        categories = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Article.objects.filter(category=categories)


class AuthorArticleListView(ListView):
    """
     This view list all articles in a specific category.
    """
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/author_articles.html'

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=author)


class CategoriesListView(ListView):
    """
     This view list all categories.
    """
    model = Category
    context_object_name = 'categories'
    template_name = 'blog/categories_list.html'


class AuthorsListView(ListView):
    """
     This view list all categories.
    """
    model = User
    context_object_name = 'authors'
    template_name = 'blog/authors_list.html'


class ArticleDetailView(DetailView):
    """

    """
    model = Article
