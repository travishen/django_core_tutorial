# from django.test import TestCase
#
# from posts.models import Post
#
# # Create your tests here.
#
# class PostModelTestCase(TestCase):
#     def setUp(self):
#         # test create
#         Post.objects.create(title='Test Post', slug='test-post')
#
#     def test_post_title(self):
#         obj = Post.objects.get(slug='test-post')
#         self.assertEqual(obj.title, 'Test Post')
#         self.assertTrue(obj.title == 'Test Post')
#
#     def create_post(self, **kwargs):
#         return Post.objects.create(**kwargs)
#
#     def test_slug(self):
#         obj = Post.objects.create(title='Test Slug')
#         self.assertEquals(obj.slug, 'test-slug')
#         obj.title = 'New Test Slug'
#         obj.save()
#         self.assertEquals(obj.slug, 'new-test-slug')
#
#     def test_unique(self):
#         Post.objects.create(title='Test Unique')
#         Post.objects.create(title='Test Unique')
#         qs = Post.objects.filter(title='Test Unique')
#         self.assertEqual(qs.count(), 1)


