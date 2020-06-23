# Django imports.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import View

# Blog app imports.
from blog.models.article_models import Article


class DashboardView(LoginRequiredMixin, View):
    """
    Display homepage of the dashboard.
    """
    context = {}
    template_name = 'dashboard/author/dashboard.html'

    def get(self, request, *args, **kwargs):
        """
        Returns the author details
        """

        articles_list = Article.objects.filter(author=request.user)

        total_articles_written = len(articles_list)
        total_articles_published = len(
            articles_list.filter(status=Article.PUBLISHED))
        total_articles_views = sum(article.views for article in articles_list)
        total_articles_comments = sum(
            article.comments.count() for article in articles_list)

        self.context['total_articles_written'] = total_articles_written
        self.context['total_articles_published'] = total_articles_published
        self.context['total_articles_views'] = total_articles_views
        self.context['total_articles_comments'] = total_articles_comments

        return render(request, self.template_name, self.context)


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
        return redirect('blog:dashboard_home')


class AuthorWrittenArticleView(LoginRequiredMixin, View):
    """
       Displays all articles written by an author.
    """

    def get(self, request):
        """
           Returns all articles written by an author.
        """
        template_name = 'dashboard/author/author_written_article_list.html'
        context_object = {}

        written_articles = Article.objects.filter(author=request.user.id).order_by('-date_created')
        total_articles_written = len(written_articles)

        page = request.GET.get('page', 1)

        paginator = Paginator(written_articles, 25)
        try:
            written_articles_list = paginator.page(page)
        except PageNotAnInteger:
            written_articles_list = paginator.page(1)
        except EmptyPage:
            written_articles_list = paginator.page(paginator.num_pages)

        context_object['written_articles_list'] = written_articles_list
        context_object['total_articles_written'] = total_articles_written

        return render(request, template_name, context_object)


class AuthorPublishedArticleView(LoginRequiredMixin, View):
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
                                                    status=Article.PUBLISHED)
        total_articles_published = len(published_articles)

        page = request.GET.get('page', 1)

        paginator = Paginator(published_articles, 25)
        try:
            published_articles_list = paginator.page(page)
        except PageNotAnInteger:
            published_articles_list = paginator.page(1)
        except EmptyPage:
            published_articles_list = paginator.page(paginator.num_pages)

        context_object['published_articles_list'] = published_articles_list
        context_object['total_articles_published'] = total_articles_published

        return render(request, template_name, context_object)


class AuthorDraftedArticleView(LoginRequiredMixin, View):
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
                                                  status=Article.DRAFTED)
        total_articles_drafted = len(drafted_articles)

        page = request.GET.get('page', 1)

        paginator = Paginator(drafted_articles, 25)
        try:
            drafted_articles_list = paginator.page(page)
        except PageNotAnInteger:
            drafted_articles_list = paginator.page(1)
        except EmptyPage:
            drafted_articles_list = paginator.page(paginator.num_pages)

        context_object['drafted_articles_list'] = drafted_articles_list
        context_object['total_articles_drafted'] = total_articles_drafted

        return render(request, template_name, context_object)
