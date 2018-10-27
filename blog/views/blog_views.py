# Standard Python Library imports.
from functools import reduce
import operator

# Core Django imports.
from django.contrib.auth.models import User
from django.db.models import Q
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


class ArticleSearchListView(ArticleListView):
    """
    Displays a list of articles filtered by the search query.

    It inherits the Article List View so that we can display
    the result of the user's search on the same page as the Article
    List View. It displays 10 results per page.
    It takes in a query from the user from the search bar.
    """
    paginate_by = 10
    template_name = "blog/article_search_list_view.html"

    def get_queryset(self):
        """
        Search for a user input in the search bar.

        It pass in the query value to the search view using the 'q' parameter.
        Then in the view, It searches the 'title', 'slug', 'body' and fields.

        To make the search a little smarter, say someone searches for
        'container docker ansible' and It want to search the records where all
        3 words appear in the article content in any order, It split the query
        into separate words and chain them.
        """
        search_results = super(ArticleListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            search_results = search_results.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(slug__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(body__icontains=q) for q in query_list))
            )

        return search_results



