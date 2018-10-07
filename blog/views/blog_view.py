# Third party imports.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

# Local application imports.
from blog.models.blog_model import Category, Article, Comment


class ArticleListView(ListView):
    """
     This view list all articles and categories.
    """
    context_object_name = "articles"
    queryset = Article.objects.filter(status='published')
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

