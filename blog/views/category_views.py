# Core Django imports.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView
)

# Blog application imports.
from blog.models.blog_models import Article, Category


class CategoryArticlesListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/category_articles.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Article.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super(CategoryArticlesListView, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context['category'] = category
        return context


class CategoriesListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'blog/categories_list.html'


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ["name", "image"]
    success_url = reverse_lazy("blog:categories_list")
    success_message = "Category Created Successfully"


class CategoryUpdateCreateView(LoginRequiredMixin, SuccessMessageMixin,
                               UpdateView):
    model = Category
    fields = ["name", "image"]
    success_url = reverse_lazy("blog:categories_list")
    success_message = "Category Updated Successfully"
