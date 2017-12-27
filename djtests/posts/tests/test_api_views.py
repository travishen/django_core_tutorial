from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils import timezone


from rest_framework.test import APIRequestFactory, force_authenticate

from posts.api.views import (
    PostCreateAPIView,
    PostDeleteAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostUpdateAPIView,
    )

User = get_user_model()

from posts.models import Post

class PostApiTestCase(TestCase):
    def setUp(self):
        self.data = {
            'title': 'Test API',
            'content': 'New Content',
            'publish': timezone.now().date()
        }
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            username='test_admin',
            email='test@test.test',
            password='testtest',
            is_staff=True,
            is_superuser=True
        )

    def test_get_data(self):
        obj = Post.objects.create(title='Test API Post',
                                  content='New Content',
                                  publish=timezone.now().date())

        list_url = reverse('posts-api:list')
        detail_url = reverse('posts:detail', kwargs={'slug': obj.slug})

        # get list
        request = self.factory.get(list_url)
        response = PostListAPIView.as_view()(request)
        self.assertTrue(response.status_code, 200)

        # get detail
        request = self.factory.get(detail_url)
        response = PostDetailAPIView.as_view()(request, slug=obj.slug)
        self.assertTrue(response.status_code, 200)

    def test_crud_data(self):
        obj = Post.objects.create(title='Test API Post',
                                  content='New Content',
                                  publish=timezone.now().date())

        create_url = reverse('posts-api:create')
        update_url = reverse('posts-api:update', kwargs={'slug': obj.slug})
        delete_url = reverse('posts-api:delete', kwargs={'slug': obj.slug})

        request_create = self.factory.post(create_url, data=self.data)
        force_authenticate(request_create, self.user)
        response_create = PostCreateAPIView.as_view()(request_create, slug=obj.slug)

        self.assertEqual(response_create.status_code, 201)

        request_update = self.factory.put(update_url, data=self.data)
        force_authenticate(request_update, self.user)
        response_update = PostUpdateAPIView.as_view()(request_update, slug=obj.slug)

        self.assertEqual(response_update.status_code, 200)

        request_delete = self.factory.delete(delete_url)
        force_authenticate(request_delete, self.user)
        response_delete = PostDeleteAPIView.as_view()(request_delete, slug=obj.slug)
        self.assertEqual(response_delete.status_code, 204)



