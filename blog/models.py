from django.db import models
from django.urls import reverse
from organizer.models import Tag, Startup


class GetReversedURLForSlugMixin:

	def get_reversed_url(self, path_name):
		return reverse(
			path_name,
			kwargs = {
				'year': self.pub_date.year,
				'month': self.pub_date.month,
				'slug': self.slug
			}
		)


class Post(models.Model, GetReversedURLForSlugMixin):
	title    = models.CharField(max_length=63)
	slug     = models.SlugField(
					max_length=63,
					help_text='A label for URL config',
					unique_for_month='pub_date')
	text     = models.TextField()
	pub_date = models.DateField('Published', auto_now_add=True)
	tags     = models.ManyToManyField(
		Tag,
		blank=True,
		related_name='blog_posts',
	)
	startups = models.ManyToManyField(
		Startup,
		blank=True,
		related_name='blog_posts',
	)

	class Meta:
		verbose_name  = 'blog post'
		ordering      = ['-pub_date', 'title']
		get_latest_by = 'pub_date'

	def get_absolute_url(self):
		return self.get_reversed_url('post_detail')

	def get_create_url(self):
		return self.get_reversed_url('post_create')

	def get_update_url(self):
		return self.get_reversed_url('post_update')

	def get_delete_url(self):
		return self.get_reversed_url('post_delete')

	def __str__(self):
		return f'{self.title} on {self.pub_date.strftime("%Y-%m-%d")}'
