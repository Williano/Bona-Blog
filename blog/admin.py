# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models.blog_models import Article
from .models.category_models import Category
from .models.comment_models import Comment
from .models.author_models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ['user', ]


# Registers the author profile model at the admin backend.
admin.site.register(Profile, ProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'image')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name', ]


# Registers the category model at the admin backend.
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('category', 'title', 'slug', 'author', 'image',
                    'body', 'date_published', 'status')
    list_filter = ('status', 'date_created', 'date_published', 'author',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'date_published'
    ordering = ['status', 'date_published', ]


# Registers the article model at the admin backend.
admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'comment', 'article', 'date_created', )
    list_filter = ('date_created', 'name',)
    search_fields = ('name', 'article', 'comment')
    date_hierarchy = 'date_created'
    ordering = ['date_created', ]


# Registers the comment model at the admin backend.
admin.site.register(Comment, CommentAdmin)
