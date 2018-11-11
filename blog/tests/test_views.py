# Core Django imports.
from django.contrib.auth.models import User
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

         Model mommy creates three users and store them in a
          list called authors and you can access each of them using indices.

         In the view, it returns all the users and you can access every users
         profile details through the user's model.
        """
        self.client = Client()
        self.authors = mommy.make(User, _quantity=3)

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

    def test_if_author_list_view_returns_the_right_number_of_authors(self):
        response = self.client.get(reverse('blog:authors_list'))
        self.assertEqual(len(response.context_data['authors']), 3)

    def test_if_author_list_view_returns_the_right_author_details(self):
        response = self.client.get(reverse('blog:authors_list'))
        self.assertEqual(response.context_data['authors'][0].profile,
                         self.authors[0].profile)
        self.assertEqual(response.context_data['authors'][0].first_name,
                         self.authors[0].first_name)
        self.assertEqual(response.context_data['authors'][0].last_name,
                         self.authors[0].last_name)
        self.assertEqual(response.context_data['authors'][0].email,
                         self.authors[0].email)
        self.assertEqual(response.context_data['authors'][0].username,
                         self.authors[0].username)
        self.assertEqual(response.context_data['authors'][0].profile.image,
                         self.authors[0].profile.image)


class CategoryArticlesListViewTest(TestCase):
    """
    Class to test a particular category's articles.
    """

    def setUp(self):
        """
        Set up all the tests using django client and model_mommy.
        """
        self.client = Client()
        self.category = mommy.make(Category)
        self.articles = mommy.make(Article, category=self.category, _quantity=5)

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

    def test_if_category_articles_list_view_returns_the_right_number_of_articles(self):
        response = self.client.get(reverse('blog:category_articles',
                                           kwargs={'slug': self.category.slug}))
        self.assertEqual(len(response.context_data["articles"]), 5)

    def test_if_category_articles_list_view_returns_the_right_category_details(self):
        response = self.client.get(self.category.get_absolute_url())
        self.assertEqual(response.context_data["articles"][0].category,
                         self.category)
        self.assertEqual(response.context_data["articles"][0].category.name,
                         self.category.name)
        self.assertEqual(response.context_data["articles"][0].category.slug,
                         self.category.slug)
        self.assertEqual(response.context_data["articles"][0].category.image,
                         self.category.image)

    def test_if_category_articles_list_view_returns_the_right_article_details(self):
        """
        This test checks if the view returns the right articles according to the
        date they were published.

        In the setup, model mommy creates five articles and store
        them in a list called articles. So the last article in the list will
        be the first article in the list view since it was created last by model
        mommy.
        The list view orders articles according to the time they were published
        so the last article in the articles list will be displayed first in the
        view.
        """
        response = self.client.get(self.category.get_absolute_url())
        self.assertEqual(response.context_data['articles'][0].category,
                         self.articles[4].category)
        self.assertEqual(response.context_data['articles'][0].title,
                         self.articles[4].title)
        self.assertEqual(response.context_data['articles'][0].slug,
                         self.articles[4].slug)
        self.assertEqual(response.context_data['articles'][0].author,
                         self.articles[4].author)
        self.assertEqual(response.context_data['articles'][0].image,
                         self.articles[4].image)
        self.assertEqual(response.context_data['articles'][0].body,
                         self.articles[4].body)
        self.assertEqual(response.context_data['articles'][0].date_published,
                         self.articles[4].date_published)
        self.assertEqual(response.context_data['articles'][0].date_created,
                         self.articles[4].date_created)
        self.assertEqual(response.context_data['articles'][0].status,
                         self.articles[4].status)


class AuthorArticlesListViewTest(TestCase):
    """
      Class to test a particular author's articles.
    """

    def setUp(self):
        """
        Setup all the tests using django client and model_mommy.
        """
        self.client = Client()
        self.author = mommy.make(User)
        self.articles = mommy.make(Article, author=self.author, _quantity=5)

    def test_author_article_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:author_articles',
                                           kwargs={
                                               'username':
                                                   self.author.username}
                                           )
                                   )
        self.assertEqual(response.status_code, 200)

    def test_if_author_article_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:author_articles',
                                           kwargs={
                                               'username':
                                                   self.author.username}
                                           )
                                   )
        self.assertTemplateUsed(response, 'blog/author_articles.html')

    def test_if_author_article_list_view_returns_the_right_author_details(self):
        response = self.client.get(reverse('blog:author_articles',
                                           kwargs={
                                               'username':
                                                   self.author.username}
                                           )
                                   )

        self.assertEqual(response.context_data["articles"][0].author.id,
                         self.author.id)
        self.assertEqual(response.context_data["articles"][0].author.first_name,
                         self.author.first_name)
        self.assertEqual(response.context_data["articles"][0].author.last_name,
                         self.author.last_name)
        self.assertEqual(response.context_data["articles"][0].author.email,
                         self.author.email)
        self.assertEqual(response.context_data["articles"][0].author.username,
                         self.author.username)
        self.assertEqual(response.context_data["articles"][0].author.profile.image,
                         self.author.profile.image)

    def test_if_author_article_list_view_returns_the_right_article_details(self):
        """
        This test checks if the view returns the right articles according to the
        date they were published.

        In the setup, model mommy creates five articles and store
        them in a list called articles. So the last article in the list will
        be the first article in the list view since it was created last by model
        mommy.
        The list view orders articles according to the time they were published
        so the last article in the articles list will be displayed first in the
        view.
        """
        response = self.client.get(reverse('blog:author_articles',
                                           kwargs={
                                               'username':
                                                   self.author.username}
                                           )
                                   )

        self.assertEqual(response.context_data['articles'][0].author,
                         self.articles[4].author)
        self.assertEqual(response.context_data['articles'][0].title,
                         self.articles[4].title)
        self.assertEqual(response.context_data['articles'][0].slug,
                         self.articles[4].slug)
        self.assertEqual(response.context_data['articles'][0].author,
                         self.articles[4].author)
        self.assertEqual(response.context_data['articles'][0].image,
                         self.articles[4].image)
        self.assertEqual(response.context_data['articles'][0].body,
                         self.articles[4].body)
        self.assertEqual(response.context_data['articles'][0].date_published,
                         self.articles[4].date_published)
        self.assertEqual(response.context_data['articles'][0].date_created,
                         self.articles[4].date_created)
        self.assertEqual(response.context_data['articles'][0].status,
                         self.articles[4].status)


class ArticleDetailViewTest(TestCase):
    """
    Test to check if the article detail view works as required.
    """
    def setUp(self):
        """
        Model mommy creates an article.

        :return: an article
        """
        self.client = Client()
        self.article = mommy.make(Article)

    def test_article_detail_view_absolute_url(self):
        response = self.client.get(self.article.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_article_detail_view_url_by_name(self):
        response = self.client.get(reverse('blog:article_detail',
                                           kwargs={'slug': self.article.slug}))
        self.assertEqual(response.status_code, 200)

    def test_if_categories_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:article_detail',
                                           kwargs={'slug': self.article.slug}))
        self.assertTemplateUsed(response, 'blog/article_detail.html')

    def test_if_article_detail_view_returns_the_right_article_details(self):
        response = self.client.get(self.article.get_absolute_url())
        self.assertEqual(response.context["article"].category,
                         self.article.category)
        self.assertEqual(response.context["article"].title, self.article.title)
        self.assertEqual(response.context["article"].slug, self.article.slug)
        self.assertEqual(response.context["article"].author,
                         self.article.author)
        self.assertEqual(response.context["article"].image, self.article.image)
        self.assertEqual(response.context["article"].body, self.article.body)
        self.assertEqual(response.context["article"].date_published,
                         self.article.date_published)
        self.assertEqual(response.context["article"].date_created,
                         self.article.date_created)
        self.assertEqual(response.context["article"].status,
                         self.article.status)


class ArticleSearchListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.articles = mommy.make(Article, _quantity=5, status='PUBLISHED')

    def test_article_search_list_view_status_code(self):
        response = self.client.get("/search/")
        self.assertEqual(response.status_code, 200)

    def test_article_search_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:article_search_list_view'))
        self.assertEqual(response.status_code, 200)

    def test_article_search_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:article_search_list_view'))
        self.assertTemplateUsed(response, 'blog/article_search_list_view.html')

    def test_article_search_list_view_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('blog:article_search_list_view'))
        self.assertNotContains(response, 'blog/categories_list_view.html')

    def test_article_search_list_view_returns_the_right_query_results(self):
        response = self.client.get(f"/search/?q={self.articles[0].slug}")
        self.assertEqual(len(response.context_data['articles']), 1)
        self.assertEqual(response.context_data['articles'][0].title,
                         self.articles[0].title)

    def test_article_search_list_view_returns_all_articles_if_nothing_is_typed_in_the_search_input(self):
        response = self.client.get(f"/search/?q=")
        self.assertEqual(len(response.context_data['articles']), 5)


