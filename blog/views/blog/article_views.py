# Standard Python Library imports.
from functools import reduce
import operator

# Core Django imports.
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone
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
from blog.models.article_models import Article
from blog.forms.blog.article_forms import (
    ArticleCreateForm,
    ArticleUpdateForm,
)
from blog.models.category_models import Category
from blog.forms.blog.comment_forms import CommentForm


class ArticleListView(ListView):
    context_object_name = "articles"
    paginate_by = 12
    queryset = Article.objects.filter(status=Article.PUBLISHED)
    template_name = "blog/article/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(approved=True)
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article/article_detail.html'

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


class ArticleSearchListView(ListView):
    model = Article
    paginate_by = 12
    context_object_name = 'search_results'
    template_name = "blog/article/article_search_list.html"

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

        query = self.request.GET.get('q')

        if query:
            query_list = query.split()
            search_results = Article.objects.filter(
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

    def get_context_data(self, **kwargs):
        """
            Add categories to context data
        """
        context = super(ArticleSearchListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(approved=True)
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):

    template_name = 'blog/article/article_create_form.html'
    form_class = ArticleCreateForm
    object = None

    PREVIEW = "PREVIEW"
    SAVE_AS_DRAFT = "SAVE_AS_DRAFT"
    PUBLISH = "PUBLISH"

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['article_form'] = self.form_class()
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        action = self.request.POST.get("action")

        if action == self.PREVIEW:

            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            body = form.cleaned_data['body']
            tags = form.cleaned_data['tags']
            status = form.cleaned_data['status']

            article_object = Article(title=title, category=category,
                                     body=body, status=status,
                                     tags=tags)

            article_preview = {"title": article_object.title,
                               "category": str(article_object.category),
                               "body": article_object.body,
                               "tags": article_object.tags,
                               "status": article_object.status
                               }

            return JsonResponse(data=article_preview)

        if action == self.SAVE_AS_DRAFT:
            template_name = 'blog/article/article_create_form.html'
            context_object = {'form': form}

            if form.instance.status == Article.DRAFTED:

                form.instance.author = self.request.user
                form.instance.date_published = None
                form.instance.save()
                messages.success(self.request, f"'{form.instance.title}'"
                                               f" successfully saved as Draft.")
                return redirect("blog:drafted_articles")
            else:
                messages.error(self.request,
                               "You saved the article as draft but selected "
                               "the status as 'PUBLISHED'. You can't save an "
                               "article whose status is 'PUBLISHED' as draft. "
                               "Please change the status to 'DRAFT' before you "
                               "save the article as draft.")
                return render(self.request, template_name, context_object)

        if action == self.PUBLISH:
            template_name = 'blog/article/article_create_form.html'
            context_object = {'form': form}

            if form.instance.status == Article.PUBLISHED:
                form.instance.author = self.request.user
                form.instance.save()
                messages.success(self.request, f"'{form.instance.title}' "
                                               f"published successfully.")
                return redirect(to="blog:dashboard_article_detail", slug=form.instance.slug)
            else:
                messages.error(self.request,
                               "You clicked on 'PUBLISH' to publish the article"
                               " but selected the status as 'DRAFT'. "
                               "You can't Publish an article whose status is "
                               "'DRAFT'. Please change the status to "
                               "'PUBLISHED' before you can Publish the "
                               "article.")
                return render(self.request, template_name, context_object)

        return HttpResponseBadRequest


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Article
    form_class = ArticleUpdateForm
    template_name = 'blog/article/article_update_form.html'

    PREVIEW = "PREVIEW"
    SAVE_AS_DRAFT = "SAVE_AS_DRAFT"
    PUBLISH = "PUBLISH"

    def form_valid(self, form):
        action = self.request.POST.get("action")

        if action == self.PREVIEW:
            
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']
            body = form.cleaned_data['body']
            tags = form.cleaned_data['tags']
            status = form.cleaned_data['status']

            article_object = Article(title=title, category=category,
                                     image=image, body=body, status=status,
                                     tags=tags)

            article_preview = {"title": article_object.title,
                               "category": str(article_object.category),
                               "image": str(article_object.image),
                               "body": article_object.body,
                               "tags": article_object.tags,
                               "status": article_object.status
                               }

            return JsonResponse(data=article_preview)

        elif action == self.SAVE_AS_DRAFT:

            if form.instance.status == Article.DRAFTED:
                form.instance.author = self.request.user
                form.instance.date_published = None
                form.instance.save()
                messages.success(self.request, f"'{form.instance.title}'"
                                               f" successfully saved as Draft.")
                return redirect("blog:drafted_articles")
            else:
                template_name = 'blog/article/article_update_form.html'
                context_object = {'form': form}

                messages.error(self.request,
                               "You saved the article as draft but selected "
                               "the status as 'PUBLISHED'. You can't save an "
                               "article whose status is 'PUBLISHED' as draft. "
                               "Please change the status to 'DRAFT' before you "
                               "save the article as draft.")
                return render(self.request, template_name, context_object)

        elif action == self.PUBLISH:
            template_name = 'blog/article/article_update_form.html'
            context_object = {'form': form}

            if form.instance.status == Article.PUBLISHED:
                form.instance.author = self.request.user
                form.instance.date_published = timezone.now()
                form.instance.save()
                messages.success(self.request, f"'{form.instance.title}' "
                                               f"updated successfully.")
                return redirect(to="blog:dashboard_article_detail", slug=form.instance.slug)
            else:
                messages.error(self.request,
                               "You clicked on 'PUBLISH' to publish the article"
                               " but selected the status as 'DRAFT'. "
                               "You can't Publish an article whose status is "
                               "'DRAFT'. Please change the status to "
                               "'PUBLISHED' before you can Publish the "
                               "article.")
                return render(self.request, template_name, context_object)

        else:
            return HttpResponseBadRequest

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
    template_name = "blog/article/article_confirm_delete.html"

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


class TagArticlesListView(ListView):
    """
        List articles related to a tag.
    """
    model = Article
    paginate_by = 12
    context_object_name = 'tag_articles_list'
    template_name = 'blog/article/tag_articles_list.html'

    def get_queryset(self):
        """
            Filter Articles by tag_name
        """

        tag_name = self.kwargs.get('tag_name', '')

        if tag_name:
            tag_articles_list = Article.objects.filter(tags__name__in=[tag_name])

            if not tag_articles_list:
                messages.info(self.request, f"No Results for '{tag_name}' tag")
                return tag_articles_list
            else:
                messages.success(self.request, f"Results for '{tag_name}' tag")
                return tag_articles_list
        else:
            messages.error(self.request, "Invalid tag")
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(approved=True)
        return context
