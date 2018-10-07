# Third party imports.
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

