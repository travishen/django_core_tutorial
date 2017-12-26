# from django.test import TestCase
#
# from django.utils import timezone
#
# from posts.models import Post
# from posts.forms import PostForm
#
# # Create your tests here.
#
#
# class PostFormTestCase(TestCase):
#     def test_valid_form(self):
#         obj = Post.objects.create(title='Test Form', slug='test-form')
#         data = {
#             'title': obj.title,
#             'slug': obj.slug,
#             'publish': obj.publish,
#             'content': ''
#         }
#         form = PostForm(data=data)
#         self.assertTrue(form.is_valid())
#         if not form.is_valid():
#             print(form.errors)
#         self.assertEqual(form.cleand_data.get('title'), obj.title)
#
