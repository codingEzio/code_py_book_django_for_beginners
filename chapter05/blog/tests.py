from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


from .models import Post


class BlogTests(TestCase):
    """ Let's break down the modules we've imported!

    django.test
        Client      dummy browser for stimulating 'GET', 'POST'
        TestCase	well, just use it!  #TODO clarify needed
    """

    def setUp(self):

        # Kinda like 'creating' a superuser, right? (not sure)
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        """ In comparison to `models.CharField(max_length=200)`
        """

        post = Post(title='A sample title')

        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        """ Test::do-we-insert-it-correctly?
        """

        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        """ Test::can-we-access-the-index-page?
        """

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        """ Test::can-we-access-the-post-by-specific-post-id
        """

        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
