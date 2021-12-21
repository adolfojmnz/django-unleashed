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
    slug = models.SlugField(max_length=31, unique=True,
                   help_text='A label for URL config.')

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return self.get_reversed_url(url_path_name='tag_detail')

    def get_create_url(self):
        return self.get_reversed_url(url_path_name='tag_create')

    def get_update_url(self):
        return self.get_reversed_url(url_path_name='tag_update')

    def get_delete_url(self):
        return self.get_reversed_url(url_path_name='tag_delete')

    def __str__(self):
        return self.name.title()


class Startup(models.Model, GetReversedURLForSlugMixin):
    name         = models.CharField(max_length=31)
    slug         = models.SlugField()
    description  = models.TextField()
    founded_date = models.DateField(help_text='Date format: DD/MM/YYYY')
    contact      = models.EmailField(max_length=254)
    website      = models.URLField()
    tags         = models.ManyToManyField(Tag)

    class Meta:
        ordering      = ['name']
        get_latest_by = 'founded_date'

    def get_absolute_url(self):
        return self.get_reversed_url(url_path_name='startup_detail')

    def get_create_url(self):
        return self.get_reversed_url(url_path_name='startup_create')

    def get_update_url(self):
        return self.get_reversed_url(url_path_name='startup_update')

    def get_delete_url(self):
        return self.get_reversed_url(url_path_name='startup_delete')

    def __str__(self):
        return self.name

class NewsLink(models.Model):
    title        = models.CharField(max_length=63)
    pub_date     = models.DateField('publication date')
    link         = models.URLField(max_length=255)
    startup      = models.ForeignKey(Startup, on_delete=models.CASCADE)

    class Meta:
        verbose_name  = 'news article'
        ordering      = ['-pub_date']
        get_latest_by = 'pub_date'

    def get_absolute_url(self):
        return reverse('newslink_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('newslink_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('newslink_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title} >> {self.startup}'
