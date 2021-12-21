from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404


class GetObjectMixin:

    def get_model_object(self, slug):
        try:
            return get_object_or_404(
                self.model,
                slug__iexact = slug
            )
        except Http404:
            raise Http404('Object Not Found!')


class MethodsForHttpRequestsMixin(GetObjectMixin):
    model         = None
    form_class    = None
    template_name = ''
    context_name  = ''
    redirect_to   = ''

    def get(self, request, **kwargs):
        if kwargs:
            object = self.get_model_object(**kwargs)
            if self.form_class:
                context = {
                    'form': self.form_class(instance=object),
                    f'{self.context_name}': object
                }
            else:
                context = {
                    f'{self.context_name}': object
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
                    f'{self.context_name}': object
                }
                return render(request, self.template_name, context)
        else:
            form = self.form_class(request.POST)
            if form.is_valid():
                new_object = form.save()
                return redirect(new_object)
            else:
                context = {'form': form}
                return render(request, self.template_name, context)

    def post_delete(self, request, **kwargs):
        self.get_model_object(**kwargs).delete()
        return redirect(self.redirect_to)


class ObjectListMixin:

    def get(self, request):
        context = {
            f'{self.context_name}': self.model.objects.all()
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
