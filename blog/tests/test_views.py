# Core Django imports.
from django.test import Client
from django.test import TestCase
from django.urls import reverse

# Third-party Django app imports.
from model_mommy import mommy

# Blog application imports.
from blog.models.blog_models import Article, Category, Comment


class ArticleListViewTests(TestCase):
    """
    Class to test the list of all articles.
    """

    def setUp(self):
        """
        Set up all the tests using django client.
        """
        self.client = Client()


    def test_article_list_view_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_article_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)

    def test_if_article_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:home'))
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_if_article_list_view_does_not_contain_incorrect_html(self):
        response = self.client.get('')
        self.assertNotContains(response, "<title>BONA</title>")


class CategoriesListViewTests(TestCase):
    """
    Class to test the list of all categories
    """

    def setUp(self):
        """
        Set up all the tests using django client.
        """
        self.client = Client()

    def test_categories_list_view_status_code(self):
        response = self.client.get("/categories-list/")
        self.assertEqual(response.status_code, 200)

    def test_categories_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertEqual(response.status_code, 200)

    def test_if_categories_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertTemplateUsed(response, 'blog/categories_list.html')

    def test_if_categories_list_view_does_not_contain_incorrect_html(self):
        response = self.client.get('')
        self.assertNotContains(response, "<title>BONA</title>")


class AuthorsListViewTests(TestCase):
    """
    Class to test the list of all authors
    """

    def setUp(self):
        """
         Set up all the test using django client
        """
        self.client = Client()

    def test_authors_list_view_status_code(self):
        response = self.client.get("/authors-list/")
        self.assertEqual(response.status_code, 200)

    def test_authors_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:authors_list'))
        self.assertEqual(response.status_code, 200)

    def test_if_authors_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:authors_list'))
        self.assertTemplateUsed(response, 'blog/authors_list.html')

    def test_if_authors_list_view_does_not_contain_incorrect_html(self):
        response = self.client.get('')
        self.assertNotContains(response, "<title>BONA</title>")


class CategoryArticleListViewTest(TestCase):
    """
    Class to test a particular category's articles.
    """

    def setUp(self):
        """
        Set up all the tests using django client and model_mommy.
        """
        self.client = Client()
        self.category = mommy.make(Category)

    def test_category_article_list_view_status_code(self):
        response = self.client.get(self.category.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_category_article_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:category_articles',
                                           kwargs={'slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)

    def test_if_category_article_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:category_articles',
                                           kwargs={'slug': self.category.slug}))
        self.assertTemplateUsed(response, 'blog/category_articles.html')


class AuthorArticleListViewTest(TestCase):
    """
      Class to test a particular author's articles.
    """

    def setUp(self):
        """
        Setup all the tests using django client and model_mommy.
        """
        self.client = Client()
        self.article = mommy.make(Article)

    def test_author_article_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:author_articles',
                                           kwargs={
                                               'username':
                                                   self.article.author.username}
                                           )
                                   )
        self.assertEqual(response.status_code, 200)

    def test_if_author_article_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:author_articles',
                                           kwargs={
                                               'username':
                                                   self.article.author.username}
                                           )
                                   )
        self.assertTemplateUsed(response, 'blog/author_articles.html')
