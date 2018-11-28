from django.test import TestCase
from django.urls import reverse


from .models import Post


class PostModelTest(TestCase):

    # It's just for enabling us to run subseq tests 
    def setUp(self):
        Post.objects.create(text="a simple test")

    # any func starts with 'test*' and in the 'tests.py'
    #   will be tested while running the 'python manage.py test'
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'a simple test')


class HomePageView(TestCase):

    def setUp(self):
        Post.objects.create(text='yet another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
