from django.db import models


class Tag(models.Model):
    name         = models.CharField(max_length=31, unique=True)
    slug         = models.SlugField(max_length=31, unique=True,
                           help_text='A label for URL config.')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Startup(models.Model):
    name         = models.CharField(max_length=31)
    slug         = models.SlugField()
    description  = models.TextField()
    founded_date = models.DateField()
    contact      = models.EmailField(max_length=254)
    website      = models.URLField()
    tags         = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        ordering      = ['name']
        get_latest_by = 'founded_date'

class NewsLink(models.Model):
    title        = models.CharField(max_length=63)
    pub_date     = models.DateField('publication date')
    link         = models.URLField(max_length=255)
    startup      = models.ForeignKey(Startup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} >> {self.startup}'

    class Meta:
        verbose_name  = 'news article'
        ordering      = ['-pub_date']
        get_latest_by = 'pub_date'


