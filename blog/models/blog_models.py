# Core Django imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Third party app imports
from taggit.managers import TaggableManager


class Category(models.Model):
    """
     Create a category model
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    image = models.ImageField(default='category-default.jpg',
                              upload_to='category_images')

    class Meta:
        """
        Specifies various model-specific options for the Category Model.
        """
        unique_together = ('name', 'slug')
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """
        Returns a human-readable representation of the Category Model.

        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the default save method and generate the slug field
        automatically when a category is saved.

        Allows unicode in slug field. Ex: If value is category name is
        "&* World", the output will be "&*-world".

        """
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of category.

        """
        return reverse('blog:category_articles',
                       kwargs={'slug': self.slug})


class Article(models.Model):
    """
      Create an article model.
    """
    # CHOICES
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
    )

    # BLOG MODEL FIELDS
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='articles')
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='articles')
    image = models.ImageField(default='article-default.jpg',
                              upload_to='article_pics')
    body = models.TextField(null=False, blank=False)
    tags = TaggableManager()
    date_published = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        """
        Specifies various model-specific options for the Article Model.
        """
        unique_together = ("title", "slug",)
        ordering = ('-date_published',)

    def __str__(self):
        """
        Returns a human-readable representation of the blog model.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Overrides the default save method and generate the slug field
        automatically when a category is saved.

        Allows unicode in slug field. Ex: If value is category name is
        "&* World", the output will be "&*-world".

        """
        self.slug = slugify(self.title, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of article.

        """
        return reverse('blog:article_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    """
      Create a Comment model.
    """
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField()
    comment = models.TextField(null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Specifies various model-specific options for the Comment Model.
        """
        ordering = ('-date_created',)

    def __str__(self):
        """
        Returns a human-readable representation of the Comment Model.

        """
        return f"Comment by {self.name} on {self.article}"
