# Core Django imports.
from django.contrib.auth import views as auth_views
from django.urls import path

# Blog application imports.
from blog.views.blog.blog_views import (
    ArticleListView,
    ArticleDetailView,
    ArticleSearchListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    TagArticlesListView,
)

from blog.views.blog.category_views import (
    CategoryArticlesListView,
    CategoriesListView,
    CategoryCreateView,
    CategoryUpdateCreateView,
)

from blog.views.blog.author_views import (
    AuthorArticlesListView,
    AuthorsListView,
)

from blog.views.blog.comment_views import (
    CommentCreateView,
)

from blog.views.dashboard.author.index import (
    Index,

)

# Specifies the app name for name spacing.
app_name = "blog"

# article/urls.py
urlpatterns = [

    # ARTICLE URLS #

    # /home/
    path(
        route='',
        view=ArticleListView.as_view(),
        name='home'
    ),

    # /article/<str:slug>/
    path(
        route='bona/<str:slug>/',
        view=ArticleDetailView.as_view(),
        name='article_detail'

    ),

    # /search/?q=query/
    path(
        route='article/search/',
        view=ArticleSearchListView.as_view(),
        name='article_search_list_view'

     ),

    # /article-new/
    path(
        route='article/new/',
        view=ArticleCreateView.as_view(),
        name="article_create"
    ),

    # /article/<str:slug>/update/
    path(
        route='article/<str:slug>/update/',
        view=ArticleUpdateView.as_view(),
        name="article_update"
    ),

    # /article/<str:slug>/delete/
    path(
        route='article/<str:slug>/delete/',
        view=ArticleDeleteView.as_view(),
        name="article_delete"
    ),

    # /tag/<str:tag_name>/
    path(
        route='tag/<str:tag_name>/articles',
        view=TagArticlesListView.as_view(),
        name="tag_articles"
    ),


    # AUTHORS URLS #

    # /authors-list/
    path(
        route='authors/list/',
        view=AuthorsListView.as_view(),
        name='authors_list'
    ),

    # /author/<str:username>/
    path(
        route='author/<str:username>/articles',
        view=AuthorArticlesListView.as_view(),
        name='author_articles'
     ),


    # CATEGORY URLS #

    # category-articles/<str:slug>/
    path(
        route='category/<str:slug>/articles',
        view=CategoryArticlesListView.as_view(),
        name='category_articles'
    ),

    # /categories-list/
    path(
        route='categories/list/',
        view=CategoriesListView.as_view(),
        name='categories_list'
    ),

    # /category/new/
    path(
        route='category/new/',
        view=CategoryCreateView.as_view(),
        name="category_create"
    ),

    # /category/<str:slug>/update/
    path(
        route='category/<str:slug>/update/',
        view=CategoryUpdateCreateView.as_view(),
        name="category_update"
    ),




    # COMMENT URLS #

    # /comment/new/
    path(
        route='comment/new/<str:slug>/',
        view=CommentCreateView.as_view(),
        name="comment_create"
    ),



    # ACCOUNTS URLS #

    # Url for login
    path(
        route='accounts/login/',
        view=auth_views.LoginView.as_view(template_name='account/login.html'),
        name='login'
    ),



    # DASHBOARD URLS #

    # /author/dashboard/
    path(
        route="author/dashboard/",
        view=Index.as_view(),
        name="dashboard_home"
    )
]
