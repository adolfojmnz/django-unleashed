from django.core.exceptions import ValidationError
from django import forms

class TagForm(forms.Form):
    name = forms.CharField(max_length=31)
    slug = forms.SlugField(max_length=31,
                  help_text='A label for URL config.')

    def save(self):
        new_tag = Tag.objects.create(
                name=self.cleaned_data['name'],
                slug=self.cleaned_data['slug'],
        )
        return new_tag

    def clean_name(self):
        return self.clean_data['name'].lower()

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug "create" is not allowed.')
        return new_slug

