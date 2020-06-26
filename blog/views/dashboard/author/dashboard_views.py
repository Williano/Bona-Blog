# Django imports.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import View, UpdateView, CreateView, DeleteView

# Blog app imports.
from blog.forms.blog.article_forms import ArticleUpdateForm, ArticleCreateForm
from blog.models.article_models import Article


class DashboardHomeView(LoginRequiredMixin, View):
    """
    Display homepage of the dashboard.
    """
    context = {}
    template_name = 'dashboard/author/dashboard_home.html'

    def get(self, request, *args, **kwargs):
        """
        Returns the author details
        """

        articles_list = Article.objects.filter(author=request.user)

        total_articles_written = len(articles_list)
        total_articles_published = len(
            articles_list.filter(status=Article.PUBLISHED, deleted=False))
        total_articles_views = sum(article.views for article in articles_list)
        total_articles_comments = sum(
            article.comments.count() for article in articles_list)

        recent_published_articles_list = articles_list.filter(
            status=Article.PUBLISHED, deleted=False).order_by("-date_published")[:5]

        self.context['total_articles_written'] = total_articles_written
        self.context['total_articles_published'] = total_articles_published
        self.context['total_articles_views'] = total_articles_views
        self.context['total_articles_comments'] = total_articles_comments
        self.context['recent_published_articles_list'] = recent_published_articles_list

        return render(request, self.template_name, self.context)


class ArticleWriteView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/author/article_create_form.html'
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
            template_name = 'dashboard/author/article_create_form.html'
            context_object = {'form': form}

            if form.instance.status == Article.DRAFTED:
                form.instance.author = self.request.user
                form.instance.tags = form.cleaned_data['tags']
                form.instance.date_published = None
                form.instance.save()
                messages.success(self.request, f"Article drafted successfully.")
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
            template_name = 'dashboard/author/article_create_form.html'
            context_object = {'form': form}

            if form.instance.status == Article.PUBLISHED:
                form.instance.author = self.request.user
                form.instance.save()
                messages.success(self.request, f"Article published successfully.")
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
    template_name = 'dashboard/author/article_update_form.html'

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
                form.instance.tags = form.cleaned_data['tags']
                form.instance.date_published = None
                form.instance.save()
                messages.success(self.request, f"Article drafted successfully.")
                return redirect("blog:drafted_articles")
            else:
                template_name = 'dashboard/author/article_update_form.html'
                context_object = {'form': form}

                messages.error(self.request,
                               "You saved the article as draft but selected "
                               "the status as 'PUBLISHED'. You can't save an "
                               "article whose status is 'PUBLISHED' as draft. "
                               "Please change the status to 'DRAFT' before you "
                               "save the article as draft.")
                return render(self.request, template_name, context_object)

        elif action == self.PUBLISH:
            template_name = 'dashboard/author/article_update_form.html'
            context_object = {'form': form}

            if form.instance.status == Article.PUBLISHED:
                form.instance.author = self.request.user
                form.instance.date_published = timezone.now()
                form.instance.save()
                messages.success(self.request, f"Article updated successfully.")
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


class ArticleDeleteView(LoginRequiredMixin, View):
    """
      Deletes article
    """

    def get(self, *args, **kwargs):
        """
           Checks if user who has requested to delete the article is the
           owner of the article.
           If the user is the owner, it sets the deleted field of the article to true and
           return a successful message.
           If the user is not the owner, it tells user he/she can't delete it
        """
        article = get_object_or_404(Article, slug=self.kwargs.get("slug"))

        if self.request.user == article.author.username:
            messages.error(request=self.request, message="You do not have permission to delete this article.")
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))

        article.deleted = True
        article.save()

        messages.success(request=self.request, message="Article Deleted Successfully")
        return redirect(to='blog:deleted_articles')


class DashboardArticleDetailView(LoginRequiredMixin, View):
    """
       Displays article details.
    """

    def get(self, request, *args, **kwargs):
        """
           Returns article details.
        """
        template_name = 'dashboard/author/dashboard_article_detail.html'
        context_object = {}

        article = get_object_or_404(Article, slug=self.kwargs.get("slug"))

        context_object['article_title'] = article.title
        context_object['article'] = article

        return render(request, template_name, context_object)


class ArticlePublishView(LoginRequiredMixin, View):
    """
       View to publish a drafted article
    """

    def post(self, request, *args, **kwargs):
        """
            Gets article slug from user and gets the article from the
            database.
            It then sets the status to publish and date published to now and
            then save the article and redirects the author to his/her published
            articles.
        """
        article = get_object_or_404(Article, slug=self.kwargs.get('slug'))
        article.status = Article.PUBLISHED
        article.date_published = timezone.now()
        article.save()

        messages.success(request, f"'{article.title}' Published successfully.")
        return redirect('blog:published_articles')


class AuthorWrittenArticlesView(LoginRequiredMixin, View):
    """
       Displays all articles written by an author.
    """

    def get(self, request):
        """
           Returns all articles written by an author.
        """
        template_name = 'dashboard/author/author_written_article_list.html'
        context_object = {}

        written_articles = Article.objects.filter(author=request.user.id, deleted=False).order_by('-date_created')
        total_articles_written = len(written_articles)

        page = request.GET.get('page', 1)

        paginator = Paginator(written_articles, 5)
        try:
            written_articles_list = paginator.page(page)
        except PageNotAnInteger:
            written_articles_list = paginator.page(1)
        except EmptyPage:
            written_articles_list = paginator.page(paginator.num_pages)

        context_object['written_articles_list'] = written_articles_list
        context_object['total_articles_written'] = total_articles_written

        return render(request, template_name, context_object)


class AuthorPublishedArticlesView(LoginRequiredMixin, View):
    """
       Displays published articles by an author.
    """

    def get(self, request):
        """
           Returns published articles by an author.
        """
        template_name = 'dashboard/author/author_published_article_list.html'
        context_object = {}

        published_articles = Article.objects.filter(author=request.user.id,
                                                    status=Article.PUBLISHED, deleted=False).order_by('-date_published')
        total_articles_published = len(published_articles)

        page = request.GET.get('page', 1)

        paginator = Paginator(published_articles, 5)
        try:
            published_articles_list = paginator.page(page)
        except PageNotAnInteger:
            published_articles_list = paginator.page(1)
        except EmptyPage:
            published_articles_list = paginator.page(paginator.num_pages)

        context_object['published_articles_list'] = published_articles_list
        context_object['total_articles_published'] = total_articles_published

        return render(request, template_name, context_object)


class AuthorDraftedArticlesView(LoginRequiredMixin, View):
    """
       Displays drafted articles by an author.
    """

    def get(self, request):
        """
           Returns drafted articles by an author.
        """
        template_name = 'dashboard/author/author_drafted_article_list.html'
        context_object = {}

        drafted_articles = Article.objects.filter(author=request.user.id,
                                                  status=Article.DRAFTED, deleted=False).order_by('-date_published')
        total_articles_drafted = len(drafted_articles)

        page = request.GET.get('page', 1)

        paginator = Paginator(drafted_articles, 5)
        try:
            drafted_articles_list = paginator.page(page)
        except PageNotAnInteger:
            drafted_articles_list = paginator.page(1)
        except EmptyPage:
            drafted_articles_list = paginator.page(paginator.num_pages)

        context_object['drafted_articles_list'] = drafted_articles_list
        context_object['total_articles_drafted'] = total_articles_drafted

        return render(request, template_name, context_object)


class AuthorDeletedArticlesView(LoginRequiredMixin, View):
    """
       Displays deleted articles by an author.
    """

    def get(self, request):
        """
           Returns deleted articles by an author.
        """
        template_name = 'dashboard/author/author_deleted_article_list.html'
        context_object = {}

        deleted_articles = Article.objects.filter(author=request.user.id,
                                                  deleted=True).order_by('-date_published')
        total_articles_deleted = len(deleted_articles)

        page = request.GET.get('page', 1)

        paginator = Paginator(deleted_articles, 5)
        try:
            deleted_articles_list = paginator.page(page)
        except PageNotAnInteger:
            deleted_articles_list = paginator.page(1)
        except EmptyPage:
            deleted_articles_list = paginator.page(paginator.num_pages)

        context_object['deleted_articles_list'] = deleted_articles_list
        context_object['total_articles_deleted'] = total_articles_deleted

        return render(request, template_name, context_object)
