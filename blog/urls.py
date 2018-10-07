# Third party imports.
from django.urls import path

# Local application imports.
from blog.views.blog_view import (
    ArticleListView,
    CategoryArticleListView,
)

# Specifies the app name for name spacing.
app_name = "blog"

urlpatterns = [
    # /blog/home/
    path('', ArticleListView.as_view(), name='home'),

    # category/<str:slug>/
    path('category-articles/<str:slug>/', CategoryArticleListView.as_view(),
         name='category_articles'),

]
