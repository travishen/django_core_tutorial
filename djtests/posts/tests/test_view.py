from django.test import TestCase
from django.core.urlresolvers import reverse

from posts.models import Post

# Create your tests here.

class PostViewTestCase(TestCase):
    def test_list_view(self):
        url = reverse('posts:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        obj = Post.objects.create(title='Test View')
        print(obj.get_absolute_url())
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        obj = Post.objects.create(title='Test View')
        url = reverse('posts:update', kwargs={'slug': obj.slug})
        response = self.client.get(url + 'edit/')
        self.assertEqual(response.status_code, 404)
