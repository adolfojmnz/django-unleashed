from django.core.exceptions import ValidationError
from django import forms

from .models import Tag


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.clean_data['name'].lower()

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug "create" is not allowed.')
        return new_slug

