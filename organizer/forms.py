from django.core.exceptions import ValidationError
from django import forms

from .models import Tag, Startup, NewsLink


class SlugCleanMixin:
    """ Mixin class for slug cleaning method. """

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError(
                    'The slug "create" is not allowed.'
            )
        return new_slug


class TagForm(forms.ModelForm, SlugCleanMixin):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()


class StartupForm(forms.ModelForm, SlugCleanMixin):
    class Meta:
        model  = Startup
        fields = '__all__'


class NewsLinkForm(forms.ModelForm):
    class Meta:
        model  = NewsLink
        fields = '__all__'
