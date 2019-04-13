# Core Django imports.
from django.contrib.auth import views as auth_views
from django.urls import path

# Blog application imports.
from blog.views.blog_views import (
    ArticleListView,
    ArticleDetailView,
    ArticleSearchListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

from blog.views.category_views import (
    CategoryArticlesListView,
    CategoriesListView,
    CategoryCreateView,
    CategoryUpdateCreateView,
)

from blog.views.author_views import (
    AuthorArticlesListView,
    AuthorsListView,
)

# Specifies the app name for name spacing.
app_name = "blog"

# blog/urls.py
urlpatterns = [
    # /home/
    path('', ArticleListView.as_view(), name='home'),

    # category-articles/<str:slug>/
    path('category-articles/<str:slug>/', CategoryArticlesListView.as_view(),
         name='category_articles'
         ),

    # /author/<str:username>/
    path('author-articles/<str:username>/', AuthorArticlesListView.as_view(),
         name='author_articles'
         ),

    # /categories-list/
    path('categories-list/', CategoriesListView.as_view(),
         name='categories_list'
         ),

    # /authors-list/
    path('authors-list/', AuthorsListView.as_view(), name='authors_list'),

    # /article/<str:slug>/
    path('article/<str:slug>/', ArticleDetailView.as_view(),
         name='article_detail'
         ),

    # /search/?q=query/
    path('search/', ArticleSearchListView.as_view(),
         name='article_search_list_view'
         ),

    # /article-new/
    path('article-new/', ArticleCreateView.as_view(),
         name="article_create"),

    # /article/<str:slug>/update/
    path('article/<str:slug>/update/', ArticleUpdateView.as_view(),
         name="article_update"),

    # /article/<str:slug>/delete/
    path('article/<str:slug>/delete/', ArticleDeleteView.as_view(),
         name="article_delete"),

    # /category/new/
    path('category/new/', CategoryCreateView.as_view(),
         name="category_create"),

    # /category/<str:slug>/update/
    path('category/<str:slug>/update/', CategoryUpdateCreateView.as_view(),
         name="category_update"),

    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='authors/login.html'),
         name='login'),  # Url for login
]
