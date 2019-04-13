# Standard Python library imports.
from markdown import markdown

# Core Django imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.text import slugify

# Third party app imports
from taggit.managers import TaggableManager

# Blog application imports.
from blog.utils.blog_utils import count_words, get_read_time
from blog.models.category_models import Category


class Article(models.Model):

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
    tags = TaggableManager(blank=True)
    date_published = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT')
    views = models.PositiveIntegerField(default=0)
    count_words = models.PositiveIntegerField(default=0)
    read_time = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_published',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def get_body_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if instance.body:
#         html_string = instance.get_body_as_markdown()
#         read_time_var = get_read_time(html_string)
#         instance.read_time = read_time_var
#
#
# pre_save.connect(pre_save_post_receiver, sender=Article)

