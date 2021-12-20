from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm


class MethodsForHttpRequestsMixin:
	form_class    = None
	model 	      = None
	model_name    = ''
	template_name = ''

	def get_model_object(self, year, month, slug):
		try:
			object = get_object_or_404(
				self.model,
				pub_date__year  = year,
				pub_date__month = month,
				slug__iexact    = slug
			)
			return object
		except self.model.DoesNotExist:
			raise self.model.DoesNotExist

	def get_without_object(self, request):
		context = {
			'form': self.form_class()
		}
		return render(request, self.template_name, context)

	def get(self, request, year, month, slug):
		try:
			context = {
				'form': self.form_class(),
				'self.model_name': self.get_model_object(year, month, slug)
			}
			return render(request, self.template_name, context)
		except self.model.DoesNotExist:
			raise Http404(f'{request.HTTP_REFERER} not found!')

	def post_create(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_object = form.save()
			return redirect(new_object)
		else:
			context = {'form': form}
			return render(request, self.template_name, context)

	def post_update(self, request, year, month, slug):
		form = self.form_class(request.POST)
		if form.is_valid():
			updated_object = form.save()
			return redirect(updated_object)
		else:
			try:
				context = {
					'form': form,
					'self.model_name': self.get_model_object(year, month, slug),
				}
				return render(request, self.template_name, context)
			except self.model_name.DoesNotExist:
				raise Http404(f'{request.HTTP_REFERER} not found!')

	def post_delete(self, request, year, month, slug):
		try:
			self.get_model_object(year, month, slug).delete()
			return redirect(f'{self.model_name}_list')
		except self.model_name.DoesNotExist:
			raise Http404(f'{request.HTTP_REFERER} not found!')


class CreateObjectMixin(MethodsForHttpRequestsMixin):

	def get(self, request):
		return self.get_without_object(request)

	def post(self, request):
		return self.post_create(request)


class UpdateObjectMixin(MethodsForHttpRequestsMixin):

	def post(self, request, year, month, slug):
		return self.post_update(request, year, month, slug)


class DeleteObjectMixin(MethodsForHttpRequestsMixin):

	def post(self, request, year, month, slug):
		return self.post_delete(request, year, month, slug)
