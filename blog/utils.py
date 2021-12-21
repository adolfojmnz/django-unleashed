from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .forms import PostForm


class GetObjectMixin:
	model = None

	def get_model_object(self, year, month, slug):
		try:
			return (
				get_object_or_404(
					self.model,
					pub_date__year  = year,
					pub_date__month = month,
					slug__iexact    = slug
				)
			)
		except Http404:
			raise Http404(f'Object not found!')


class MethodsForHttpRequestsMixin(GetObjectMixin):
	form_class    = None
	model 	      = None
	context_name  = ''
	template_name = ''

	def get(self, request, **kwargs):
		if kwargs:
			object = self.get_model_object(**kwargs)
			context = {
				'form': self.form_class(instance=object),
				f'{self.context_name}': object
			}
		else:
			context = {
				'form': self.form_class()
			}
		return render(request, self.template_name, context)

	def post_create(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_object = form.save()
			return redirect(new_object)
		else:
			context = {'form': form}
			return render(request, self.template_name, context)

	def post_update(self, request, **kwargs):
		object = self.get_model_object(**kwargs)
		form = self.form_class(request.POST, instance=object)
		if form.is_valid():
			updated_object = form.save()
			return redirect(updated_object)
		else:
			context = {
				'form': form,
				f'{self.context_name}': object
			}
			return render(request, self.template_name, context)

	def post_delete(self, request, **kwargs):
		self.get_model_object(**kwargs).delete()
		return redirect(f'{self.context_name}')


class ObjectListMixin:
	model = None
	context_name = ''
	template_name = ''

	def get(self, request):
		context = {
			f'{self.context_name}': self.model.objects.all()
		}
		return render(request, self.template_name, context)


class ObjectDetailMixin(GetObjectMixin):
	context_name = ''
	template_name = ''

	def get(self, request, **kwargs):
		context = {
			f'{self.context_name}': self.get_model_object(**kwargs)
		}
		return render(request, self.template_name, context)


class CreateObjectMixin(MethodsForHttpRequestsMixin):

	def post(self, request):
		return self.post_create(request)


class UpdateObjectMixin(MethodsForHttpRequestsMixin):

	def post(self, request, **kwargs):
		return self.post_update(request, **kwargs)


class DeleteObjectMixin(MethodsForHttpRequestsMixin):

	def post(self, request, **kwargs):
		return self.post_delete(request, **kwargs)
