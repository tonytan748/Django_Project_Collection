from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from djangp.template.defaultfilters import slugify
from django.test import TestCase

from ..models import Post

class PostTests(TestCase):
	def setup(self):
		self.user=User.objects.create(username="test")	
	
	def create_post(self,title="Test Post",published=True):
		return Post.objects.create(
			title=title,
			author=self.user,
			published=published
		)

	def test_model_creation(self):
		post=self.create_post()
		self.assertTrue(isinstance(post,Post))
		self.assertEqual(post.__unicode__(),post.title)
		self.assertEqual(post.slug,slugify(post.title))

	def test_model_url(self):
		post=self.create_post()
		self.assertEqual(post.get_absolute_url(),reverse('blog:detail',kwargs={'slug':post.slug}))

	def test_model_manager(self):
		live_post=self.create_post()
		draft_post=self.create_post(title='Draft post',published=False)
		self.assertIn(live_post,Post.objects.live())
		self.assertNotIn(draft_post,Post.objects.live())
		
	def test_custom_slug(self):
		post=Post.objects.create(title="a post test",slug="fizzbuszz",author=self.user)
		self.assertNotEqual(post.slug,slugify(post.title))
		self.assertEqual(post.slug,'fizzbuzz')


