from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import View


class PaginatorMixin:
	paginate_by = 5
	initial_page_number = 1

	def get_page(self, request):
		paginator = Paginator(self.model.objects.all(), self.paginate_by)
		total_pages = paginator.num_pages
		try:
			page_number = request.GET.get('page')
			if int(page_number) > total_pages:
				page_number = total_pages
			elif int(page_number) < self.initial_page_number:
				raise
		except:
			page_number = self.initial_page_number

		return paginator.page(page_number)


class ConfigGCBV:

	def get_model_object(self, **kwargs):
		try:
			return get_object_or_404(
				self.model,
				**kwargs
			)
		except Http404:
			raise Http404('Object Not Found!')

	def get_context_object_name(self):
		try:
			if self.context_object_name:
				return self.context_object_name
		except AttributeError:
			try:
				return self.model._meta.model_name
			except AttributeError:
				raise ImproperlyConfigured(
					f'{self.__class__.__name__} needs model attribute'
				)

	def get_redirect_page_after_delete(self):
		app_name = self.model._meta.app_label
		model_name = self.model._meta.model_name
		return f'{model_name}_list'


class ListView(View, PaginatorMixin, ConfigGCBV):
	"""
		model, context_name and template_name need to be defined.
	"""

	def get(self, request):
		context_object_name = self.get_context_object_name()
		page = self.get_page(request)
		context = {
			context_object_name: page,
		}
		return render(request, self.template_name, context)


class DetailView(View, ConfigGCBV):
	"""
		model and template_name need to be defined.
	"""

	def get(self, request, **kwargs):
		context_object_name = self.get_context_object_name()
		context = {
			context_object_name: self.get_model_object(**kwargs),
		}
		return render(request, self.template_name, context)


class CreateView(View):
	"""
		template_name and form_class need to be defined.
	"""

	def get(self, request):
		context = {
			'form': self.form_class()
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_object = form.save()
			return redirect(new_object)
		else:
			context = {'form': form}
		return render(request, self.template_name, context)


class UpdateView(View, ConfigGCBV):
	"""
		model, template_name and form_class need to be defined.
	"""

	def get(self, request, **kwargs):
		object = self.get_model_object(**kwargs)
		context_object_name = self.get_context_object_name()
		if self.form_class:
			context = {
				'form': self.form_class(instance=object),
				context_object_name: object,
			}
		return render(request, self.template_name, context)

	def post(self, request, **kwargs):
		object = self.get_model_object(**kwargs)
		form = self.form_class(request.POST, instance=object)
		if form.is_valid():
			updated_object = form.save()
			return redirect(updated_object)
		else:
			context_object_name = self.get_context_object_name()
			context = {
				'form': form,
				context_object_name: object,
			}
		return render(request, self.template_name, context)


class DeleteView(View, ConfigGCBV):
	"""
		model, template_name and redirect_to need to be defined.
	"""

	def get(self, request, **kwargs):
		object = self.get_model_object(**kwargs)
		context_object_name = self.get_context_object_name()
		context = {
			context_object_name: object,
		}
		return render(request, self.template_name, context)

	def post(self, request, **kwargs):
		redirect_to = self.get_redirect_page_after_delete()
		object = self.get_model_object(**kwargs)
		object.delete()
		return redirect(redirect_to)
