from django.urls import reverse
from django.db import models


class GetReversedURLForSlugMixin:
	def get_reversed_url(self, url_path_name):
		return reverse(
			url_path_name,
			kwargs={'slug': self.slug}
		)


class Tag(models.Model, GetReversedURLForSlugMixin):
	name = models.CharField(max_length=31, unique=True)
	slug = models.SlugField(
		max_length=31,
		unique=True,
		help_text='A label for URL config.',
	)

	class Meta:
		ordering = ['name']

	def get_absolute_url(self):
		return self.get_reversed_url('tag_detail')

	def get_create_url(self):
		return self.get_reversed_url('tag_create')

	def get_update_url(self):
		return self.get_reversed_url('tag_update')

	def get_delete_url(self):
		return self.get_reversed_url('tag_delete')

	def __str__(self):
		return self.name.title()


class Startup(models.Model, GetReversedURLForSlugMixin):
	name         = models.CharField(max_length=31)
	slug         = models.SlugField()
	description  = models.TextField()
	founded_date = models.DateField(help_text='Date format: DD/MM/YYYY')
	contact      = models.EmailField(max_length=254)
	website      = models.URLField()
	tags         = models.ManyToManyField(Tag, blank=True)

	class Meta:
		ordering      = ['name']
		get_latest_by = 'founded_date'

	def get_absolute_url(self):
		return self.get_reversed_url('startup_detail')

	def get_create_url(self):
		return self.get_reversed_url('startup_create')

	def get_update_url(self):
		return self.get_reversed_url('startup_update')

	def get_delete_url(self):
		return self.get_reversed_url('startup_delete')

	def __str__(self):
		return self.name

class NewsLink(models.Model, GetReversedURLForSlugMixin):
	title        = models.CharField(max_length=63)
	slug         = models.SlugField(max_length=63)
	pub_date     = models.DateField('publication date')
	link         = models.URLField(max_length=255)
	startup      = models.ForeignKey(Startup, on_delete=models.CASCADE)

	class Meta:
		verbose_name  = 'news article'
		ordering      = ['-pub_date']
		get_latest_by = 'pub_date'
		unique_together = ('slug', 'startup')

	def get_absolute_url(self):
		return self.get_reversed_url('newslink_detail')

	def get_create_url(self):
		return self.get_reversed_url('newslink_create')

	def get_update_url(self):
		return self.get_reversed_url('newslink_update')

	def get_delete_url(self):
		return self.get_reversed_url('newslink_delete')

	def __str__(self):
		return f'{self.title} >> {self.startup}'
