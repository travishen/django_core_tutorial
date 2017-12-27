# from django.test import TestCase, RequestFactory
# from django.contrib.auth.models import AnonymousUser
# from django.contrib.auth import get_user_model
# from django.core.urlresolvers import reverse
#
# from posts.models import Post
# from posts.views import post_update, post_create
#
# # Create your tests here.
# User = get_user_model()
#
#
# class PostViewAdvanceTestCase(TestCase):
#     def setUp(self):
#
#         self.factory = RequestFactory()
#         self.user = User.objects.create(
#             username='test_admin',
#             email='test@test.test',
#             password='testtest',
#             is_staff=True,
#             is_superuser=True
#         )
#
#     def test_user_auth(self):
#         obj = Post.objects.create(title='Test User Auth')
#         url = reverse('posts:update', kwargs={'slug': obj.slug})
#         request = self.factory.get(url)
#         request.user = self.user
#         response = post_update(request, slug=obj.slug)
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(request.user.is_authenticated())
#
#     def test_user_anonymous(self):
#         obj = Post.objects.create(title='Test User Auth')
#         url = reverse('posts:update', kwargs={'slug': obj.slug})
#         request = self.factory.get(url)
#         request.user = AnonymousUser()
#         response = post_update(request, slug=obj.slug)
#         self.assertEqual(response.status_code, 404)
#         self.assertTrue(request.user.is_authenticated())
#
#     def test_user_post(self):
#         url = reverse('posts:create')
#         request = self.factory.post(url)
#         request.user = self.user
#         response = post_create(request)
#         self.assertEqual(response.status_code, 200)
