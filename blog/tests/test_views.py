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

        Model mommy creates a single category called category.

        Model mommy creates four articles and store them in a list called
        articles. So the last article in the list will be the first article
        in the list view since it was created last by model mommy. You can
        access the articles using their indices.
        """
        self.client = Client()
        self.category = mommy.make(Category)
        self.articles = mommy.make(Article, status='PUBLISHED',
                                   category=self.category, _quantity=4)

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

    def test_if_article_list_view_returns_the_right_number_of_categories(self):
        response = self.client.get('')
        self.assertEqual(len(response.context_data['categories']), 1)

    def test_if_article_list_view_returns_the_right_category_details(self):
        response = self.client.get('')
        self.assertEqual(response.context_data['categories'][0],
                         self.category)
        self.assertEqual(response.context_data['categories'][0].name,
                         self.category.name)
        self.assertEqual(response.context_data['categories'][0].slug,
                         self.category.slug)
        self.assertEqual(response.context_data['categories'][0].image,
                         self.category.image)

    def test_if_article_list_view_returns_the_right_number_of_articles(self):
        response = self.client.get('')
        self.assertEqual(len(response.context_data['articles']), 4)

    def test_if_article_list_view_returns_the_right_article_details(self):
        """
        This test checks if the view returns the right articles according to the
        date they were published.

        In the setup, model mommy creates four articles and store
        them in a list called articles. So the last article in the list will
        be the first article in the list view since it was created last by model
        mommy.
        The list view orders articles according to the time they were published.
        """
        response = self.client.get('')
        self.assertEqual(response.context_data['categories'][0],
                         self.category)
        self.assertEqual(response.context_data['categories'][0].name,
                         self.category.name)
        self.assertEqual(response.context_data['articles'][0].category,
                         self.articles[3].category)
        self.assertEqual(response.context_data['articles'][0].title,
                         self.articles[3].title)
        self.assertEqual(response.context_data['articles'][0].slug,
                         self.articles[3].slug)
        self.assertEqual(response.context_data['articles'][0].author,
                         self.articles[3].author)
        self.assertEqual(response.context_data['articles'][0].image,
                         self.articles[3].image)
        self.assertEqual(response.context_data['articles'][0].body,
                         self.articles[3].body)
        self.assertEqual(response.context_data['articles'][0].date_published,
                         self.articles[3].date_published)
        self.assertEqual(response.context_data['articles'][0].date_created,
                         self.articles[3].date_created)
        self.assertEqual(response.context_data['articles'][0].status,
                         self.articles[3].status)


class CategoriesListViewTests(TestCase):
    """
    Class to test the list of all categories
    """

    def setUp(self):
        """
        Set up all the tests using django client.

        Model mommy creates five categories and store them in a list called
        categories. You can access them with their indices.
        """
        self.client = Client()
        self.categories = mommy.make(Category, _quantity=5)

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

    def test_if_categories_list_view_returns_the_right_number_of_categories(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertEqual(len(response.context_data['categories']), 5)

    def test_if_categories_list_view_returns_the_right_category_details(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertEqual(response.context_data['categories'][0].name,
                         self.categories[0].name)
        self.assertEqual(response.context_data['categories'][0].slug,
                         self.categories[0].slug)


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
