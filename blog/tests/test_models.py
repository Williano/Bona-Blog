# Third party imports.
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

# Third party imports.
from model_mommy import mommy

# Local application imports.
from blog.models.author_profile_models import Profile
from blog.models.blog_models import Category, Article, Comment


class BlogTests(TestCase):

    def setUp(self):

        user1 = User.objects.create(
            username="Williano", password="@admin123"
        )

        category1 = Category.objects.create(
            name="Sports",
            image="mbuntu-4.jpg",
            slug="sports",
        )

        article1 = Article.objects.create(
            category=category1,
            title="I am coming home",
            slug="i-am-coming-home",
            author=user1,
            image="mbuntu-4.jpg",
            body="Let the games begin.",
            tags="sports, soccer",
            date_published=timezone.now(),
            date_created="2018-09-07",
            date_updated="2018-10-07",
            status="Published",
        )

        comment1 = Comment.objects.create(
            name="Bill",
            email="paawilly17@gmail.com",
            comment="Great Article",
            article=article1,
            date_created="2018-09-07",
            date_updated="2018-09-08",
            approved=True,
        )

    def test_if_category_returns_the_right_name(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.__str__(), "Sports")

    def test_if_category_returns_the_right_slug(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.slug, "sports")

    def test_if_article_returns_the_right_name(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.__str__(), "I am coming home")

    def test_if_article_returns_the_right_slug(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.slug, "i-am-coming-home")

    def test_if_comment_returns_the_right_user(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.__str__(), "Comment by Bill on "
                                            "I am coming home")


class AuthorProfileTests(TestCase):

    def setUp(self):
        self.user = mommy.make(User)
        self.profile = mommy.make(Profile)

    def test_if_user_profile_returns_the_correct_username(self):
        self.assertEqual(self.profile.__str__(),
                         f"{self.profile.user.username}'s Profile")

    def test_if_user_profile_returns_default_picture_if_user_does_not_upload_picture(self):
        self.assertEqual(self.profile.image.name, "default.jpg")

