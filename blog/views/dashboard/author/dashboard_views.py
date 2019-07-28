# Django imports.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import View

# Blog app imports.
from blog.models.blog_models import Article


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
