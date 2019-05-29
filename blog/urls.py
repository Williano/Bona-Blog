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
    TagArticlesListView,
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

from blog.views.comment_views import (
    CommentCreateView,
)


# Specifies the app name for name spacing.
app_name = "blog"

# blog/urls.py
urlpatterns = [

    # ARTICLE URLS #

    # /home/
    path('', ArticleListView.as_view(), name='home'),

    # /article/<str:slug>/
    path('<str:slug>/', ArticleDetailView.as_view(),
         name='article_detail'
         ),

    # /search/?q=query/
    path('article/search/', ArticleSearchListView.as_view(),
         name='article_search_list_view'
         ),

    # /article-new/
    path('article/new/', ArticleCreateView.as_view(),
         name="article_create"),

    # /article/<str:slug>/update/
    path('article/<str:slug>/update/', ArticleUpdateView.as_view(),
         name="article_update"),

    # /article/<str:slug>/delete/
    path('article/<str:slug>/delete/', ArticleDeleteView.as_view(),
         name="article_delete"),

    # /tag/<str:tag_name>/
    path('tag/<str:tag_name>/articles', TagArticlesListView.as_view(),
         name="tag_articles"),


    # AUTHORS URLS #

    # /authors-list/
    path('authors/list/', AuthorsListView.as_view(), name='authors_list'),

    # /author/<str:username>/
    path('author/<str:username>/articles', AuthorArticlesListView.as_view(),
         name='author_articles'
         ),


    # CATEGORY URLS #

    # category-articles/<str:slug>/
    path('category/<str:slug>/articles', CategoryArticlesListView.as_view(),
         name='category_articles'
         ),

    # /categories-list/
    path('categories/list/', CategoriesListView.as_view(),
         name='categories_list'
         ),

    # /category/new/
    path('category/new/', CategoryCreateView.as_view(),
         name="category_create"),

    # /category/<str:slug>/update/
    path('category/<str:slug>/update/', CategoryUpdateCreateView.as_view(),
         name="category_update"),


    # COMMENT URLS #

    # /comment/new/
    path('comment/new/<str:slug>/', CommentCreateView.as_view(),
         name="comment_create"),


    # ACCOUNTS URLS #

    # Url for login
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='account/login.html'),
         name='login'),
]
