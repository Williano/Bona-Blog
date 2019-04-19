# Core Django imports.
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import (
    CreateView,
)

# Blog application imports.
from blog.models.blog_models import Article
from blog.forms.comment_forms import CommentForm


class CommentCreateView(CreateView):
    http_method_names = ['post']
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = get_object_or_404(Article,
                                            slug=self.kwargs.get('slug'))
        comment.save()
        messages.success(self.request, "Comment Added successfully")
        return redirect('blog:article_detail', comment.article.slug)

