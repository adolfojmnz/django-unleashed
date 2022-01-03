from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator


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


class GetObjectMixin:

	def get_model_object(self, **kwargs):
		try:
			return get_object_or_404(
				self.model,
				**kwargs
			)
		except Http404:
			raise Http404('Object Not Found!')


class MethodsForHttpRequestsMixin(GetObjectMixin):
	model         = None
	form_class    = None
	template_name = ''
	redirect_to   = ''

	def get(self, request, **kwargs):
		if kwargs:
			object = self.get_model_object(**kwargs)
			if self.form_class:
				context = {
					'form': self.form_class(instance=object),
					self.model.__name__.lower(): object
				}
			else:
				context = {
					self.model.__name__.lower(): object
				}
		else:
			context = {
				'form': self.form_class()
			}
		return render(request, self.template_name, context)

	def post(self, request, **kwargs):
		if kwargs:
			object = self.get_model_object(**kwargs)
			form = self.form_class(request.POST, instance=object)
			if form.is_valid():
				updated_object = form.save()
				return redirect(updated_object)
			else:
				context = {
					'form': form,
					self.model.__name__.lower(): object
				}
		else:
			form = self.form_class(request.POST)
			if form.is_valid():
				new_object = form.save()
				return redirect(new_object)
			else:
				context = {'form': form}
		return render(request, self.template_name, context)

	def post_delete(self, request, **kwargs):
		object = self.get_model_object(**kwargs)
		try:
			if object.startup:
			   self.redirect_to = object.startup
		except AttributeError:
			pass
		object.delete()
		return redirect(self.redirect_to)


class ObjectListMixin(PaginatorMixin):

	def get(self, request):
		page = self.get_page(request)
		context = {
			self.context_name: page,
		}
		return render(request, self.template_name, context)


class ObjectDetailMixin(MethodsForHttpRequestsMixin):
	pass


class CreateObjectMixin(MethodsForHttpRequestsMixin):
	pass


class UpdateObjectMixin(MethodsForHttpRequestsMixin):
	pass


class DeleteObjectMixin(MethodsForHttpRequestsMixin):

	def post(self, request, **kwargs):
		return self.post_delete(request, **kwargs)
