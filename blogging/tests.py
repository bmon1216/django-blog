"""
Title:      tests.py
"""
import datetime

from django.utils.timezone import utc
from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class PostTestCase(TestCase):
    """Tests for testing the backend"""

    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    """Tests for testing the front end"""

    # the fixtures are found in blogging/fixtures
    fixtures = ["blogging_test_fixture.json"]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)

        # uses the User table from the blogging_test_fixture
        author = User.objects.get(pk=1)

        # create multiple dummy posts
        for count in range(1, 11):
            post = Post(
                title="Post %d Title" % count,
                text="foo",
                author=author,
            )

            # adjust the 'time' on the first few posts
            if count < 6:
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    # def test_list_only_published(self):
    #     response = self.client.get("/")
    #     response_text = response.content.decode(response.charset)
    #     self.assertTrue("Latest Posts" in response_text)
    #
    #     for count in range(1, 11):
    #         title = "Post %d Title" % count
    #         if count < 6:
    #             self.assertContains(response, title, count=1)
    #         else:
    #             self.assertNotContains(response, title)
    #
    # def test_details_only_published(self):
    #     """Test for posts that are published"""
    #     for count in range(1, 11):
    #         title = "Post %d Title" % count
    #         post = Post.objects.get(title=title)
    #         response = self.client.get("/posts/%d" % post.pk)
    #         if count < 6:
    #             self.assertEqual(response.status_code, 200)
    #             self.assertContains(response, title)
    #         else:
    #             self.assertEqual(response.status_code, 404)
