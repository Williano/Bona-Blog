# Standard Python Library imports.
from functools import reduce
import operator

# Core Django imports.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    DeleteView,
    CreateView,
    ListView,
    UpdateView
)

# Blog application imports.
from blog.models.blog_models import Article
from blog.models.category_models import Category
from blog.forms.comment_forms import CommentForm


class ArticleListView(ListView):
    context_object_name = "articles"
    paginate_by = 12
    queryset = Article.objects.filter(status='PUBLISHED')
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        session_key = f"viewed_article {self.object.slug}"
        if not self.request.session.get(session_key, False):
            self.object.views += 1
            self.object.save()
            self.request.session[session_key] = True

        kwargs['related_articles'] = \
            Article.objects.filter(category=self.object.category).order_by('?')[:3]
        kwargs['article'] = self.object
        kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)


class ArticleSearchListView(ArticleListView):
    paginate_by = 12
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

            if not search_results:
                messages.info(self.request, f"No results for '{query}'")
                return search_results
            else:
                messages.success(self.request, f"Results for '{query}'")
                return search_results
        else:
            messages.error(self.request, f"Sorry you did not enter any keyword")
            return []


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    fields = ["title", "category", "image", "body", "tags", "status"]
    success_url = reverse_lazy("blog:home")
    success_message = "Article Posted Successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                        SuccessMessageMixin, UpdateView):
    model = Article
    fields = ["title", "category", "image", "body", "tags", "status"]
    success_message = "Article Updated Successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
             UserPassesTextMixin checks if it is the user before allowing
             him/her to update an article.

          :return: bool:
         """
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                        SuccessMessageMixin, DeleteView):
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy("blog:home")
    success_message = "Article Deleted Successfully"

    def test_func(self):
        """
             UserPassesTextMixin checks if it is the user before allowing
             him/her to delete the article.

          :return: bool:
         """
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

