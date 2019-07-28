# Core Django imports.
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

# Third-party Django app imports.
from model_mommy import mommy

# Blog application imports.
from blog.models.article_models import Article
from blog.models.category_models import Category
from blog.models.comment_models import Comment


class BlogTests(TestCase):
    """
      Class to test the Blog model.
    """

    def setUp(self):
        """
          Set up all the tests using model_mommy.
        """
        self.user = mommy.make(User)
        self.category = mommy.make(Category)
        self.article = mommy.make(Article)
        self.comment = mommy.make(Comment)

    def test_if_category_returns_the_right_human_readable_representation(self):
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_if_category_returns_the_right_slug(self):
        self.assertEqual(self.category.slug, slugify(self.category.name))

    def test_category_get_absolute_url(self):
        self.assertEquals(self.category.get_absolute_url(),
                          reverse('blog:category_articles',
                                  kwargs={'slug': self.category.slug}))

    def test_if_article_returns_the_right_human_readable_representation(self):
        self.assertEqual(self.article.__str__(), self.article.title)

    def test_if_article_returns_the_right_slug(self):
        self.assertEqual(self.article.slug, slugify(self.article.title))

    def test_article_get_absolute_url(self):
        self.assertEquals(self.article.get_absolute_url(),
                          reverse('blog:article_detail',
                                  kwargs={'slug': self.article.slug}))

    def test_if_comment_returns_the_right_user(self):
        self.assertEqual(
            self.comment.__str__(),
            f"Comment by {self.comment.name} on {self.comment.article}")


class AuthorProfileTests(TestCase):
    """
      Class to test the AuthorProfile Model.
    """

    def setUp(self):
        """
         Set up all the tests using model_mommy.
        """
        self.user = mommy.make(User)

    def test_if_user_profile_returns_the_correct_username(self):
        self.assertEqual(self.user.profile.__str__(),
                         f"{self.user.username}'s Profile")

    def test_if_user_profile_returns_default_picture_if_user_does_not_upload_picture(self):
        self.assertEqual(self.user.profile.image.name, "profile-pic-default.jpg")

