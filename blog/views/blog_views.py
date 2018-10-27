# Core Django imports.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView

# Blog application imports.
from blog.models.blog_models import Category, Article, Comment


class ArticleListView(ListView):
    """
     Display all categories and articles.

     It display only published articles and their names, number of likes,comment
     and views they have.
    """
    context_object_name = "articles"
    queryset = Article.objects.filter(status='PUBLISHED')
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        """
        Calls the base implementation first to get a context.

        :return: dictionary: a dictionary of all categories and their ids.
        """
        context = super().get_context_data(**kwargs)
        # Get all blog categories and return it to the view.
        context['categories'] = Category.objects.all()
        return context


class CategoryArticleListView(ListView):
    """
     Display all articles for a category.

     It display the article name, title, image and the number of likes, views
      and comments the articles have.
    """
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/category_articles.html'

    def get_queryset(self):
        categories = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Article.objects.filter(category=categories)


class AuthorArticleListView(ListView):
    """
     Display all articles for an author.

     It display the article name, title, image and the number of likes, views
     and comments the articles have.
    """
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/author_articles.html'

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=author)


class CategoriesListView(ListView):
    """
     Display all article categories.

     It display their name and number of articles they have.
    """
    model = Category
    context_object_name = 'categories'
    template_name = 'blog/categories_list.html'


class AuthorsListView(ListView):
    """
     Display all authors who write articles on the website.

     It display their name and number of articles they have written.
    """
    model = User
    context_object_name = 'authors'
    template_name = 'blog/authors_list.html'


class ArticleDetailView(DetailView):
    """
     Display details of an article.

     Display the article title, image, author, body, tags, comments.
     The author can also edit or delete an article.
    """
    model = Article
