# Third party imports
from django.contrib import admin

# Local application imports.
from .models.author_profile_model import Profile
from .models.blog_model import Category, Article, Comment


class ProfileAdmin(admin.ModelAdmin):
    """
     Customize how the profile model is displayed in the admin site.

     List display shows how the profile fields will be displayed.

     List filter shows how the profiles can be filtered.

     Search fields allows users to search profiles using user names.

     Ordering orders the profiles with the users.
    """
    list_display = ('user', 'image',)
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ['user', ]


# Registers the author profile model at the admin backend.
admin.site.register(Profile, ProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):
    """
     Customize how the category model is displayed in the admin site.

     List display shows how the category fields will be displayed.

     List filter shows how the category can be filtered.

     Search fields allows users to search categories using category names.

     Ordering orders the categories with their names.
    """
    list_display = ('name', 'slug', 'image')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name', ]


# Registers the category model at the admin backend.
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    """
     Customize how the article model is displayed in the admin site.

     List display shows how the article fields will be displayed.

     List filter shows how the article can be filtered.

     Search fields allows users to search articles using article title.

     Prepopulated fields fills the slug field automatically with the title of
     the article when the user is typing the article title.

    raw_id_field allows the author field to be displayed with a lookup widget
    that can scale much better than a dropdown select input when you
    have thousands of users

    Date hierarchy allows users to search articles based on the published date.

     Ordering orders the articles with their titles.
    """
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
    """
     Customize how the article model is displayed in the admin site.

     List display shows how the article fields will be displayed.

     List filter shows how the article can be filtered.

     Search fields allows users to search articles using article title.

    Date hierarchy allows users to search articles based on the published date.

     Ordering orders the articles with their titles.
    """
    list_display = ('name', 'email', 'comment', 'article', 'date_created',
                    'approved')
    list_filter = ('approved', 'date_created', 'name',)
    search_fields = ('name', 'article', 'comment')
    date_hierarchy = 'date_created'
    ordering = ['approved', 'date_created', ]


# Registers the comment model at the admin backend.
admin.site.register(Comment, CommentAdmin)
