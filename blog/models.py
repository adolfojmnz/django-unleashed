from django.db import models
from organizer.models import Tag, Startup


class Post(models.Model):
    title    = models.CharField(max_length=63)
    slug     = models.SlugField(
                    max_length=63,
                    help_text='A label for URL config',
                    unique_for_month='pub_date')
    text     = models.TextField()
    pub_date = models.DateField('publication date', auto_now_add=True)
    tags     = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    def get_absolute_url(self):
        return reverse('post_detail',
                kwargs={
                    'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug,
                }
        )

    def __str__(self):
        return f'{self.title} on {self.pub_date.strftime("%Y-%m-%d")}'

    class Meta:
        verbose_name  = 'blog post'
        ordering      = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

