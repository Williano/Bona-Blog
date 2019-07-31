# Core Django imports.
from django.contrib.auth import views as auth_views
from django.urls import path

# Blog application imports.
from blog.views.blog.article_views import (
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
    ArticleCommentList
)

from blog.views.dashboard.author.dashboard_views import (
    DashboardView,
    ArticlePublishView,
    AuthorWrittenArticleView,
    AuthorPublishedArticleView,
    AuthorDraftedArticleView,

)

from blog.views.account.author_profile_views import (
    AuthorProfileUpdateView,
    AuthorProfileView,
)

from blog.views.account.logout_view import UserLogoutView

from blog.views.account.login_view import UserLoginView


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
        route='article/create/',
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
        route='category/create/',
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

    # /<str:slug>/comments/
    path(
        route='<str:slug>/comments/',
        view=ArticleCommentList.as_view(),
        name="article_comments"
    ),


    # ACCOUNTS URLS #

    # accounts/login/
    path(
        route='accounts/login/',
        view=UserLoginView.as_view(),
        name='login'
    ),

    # accounts/logout/
    path(
        route='accounts/login/',
        view=UserLogoutView.as_view(),
        name='logout'
    ),

    # author/profile/update/
    path(
        route='author/profile/update/',
        view=AuthorProfileUpdateView.as_view(),
        name='author_profile_update'
    ),


    # Url for password reset.
    path('account/password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html'),
         name='password_reset'),

    # Url for successful password reset.
    path('account/password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    # Url for successful password reset confirm.
    path('account/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),

    # Url for password reset done.
    path('account/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),



    # DASHBOARD URLS #

    # /author/dashboard/
    path(
        route="author/dashboard/",
        view=DashboardView.as_view(),
        name="dashboard_home"
    ),

    # author/profile/details
    path(
        route='author/profile/details/',
        view=AuthorProfileView.as_view(),
        name='author_profile_details'
    ),

    # /article/<str:slug>/publish/
    path(
        route="article/<str:slug>/publish/",
        view=ArticlePublishView.as_view(),
        name="publish_article"
    ),

    # /author/articles/written/
    path(
        route="author/articles/written/",
        view=AuthorWrittenArticleView.as_view(),
        name="written_articles"
    ),

    # /author/articles/published/
    path(
        route="author/articles/published/",
        view=AuthorPublishedArticleView.as_view(),
        name="published_articles"
    ),

    # /author/articles/drafted/
    path(
        route="author/articles/drafted/",
        view=AuthorDraftedArticleView.as_view(),
        name="drafted_articles"
    ),

]
