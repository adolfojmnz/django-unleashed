from django.shortcuts import render, redirect, get_object_or_404


class MethodsForHttpRequestsMixin:
    model         = None
    form_class    = None
    template_name = ''
    model_name    = ''

    def get_model_object(self, slug):
        try:
            object = get_object_or_404(self.model, slug__iexact=slug)
            return object
        except self.model.DoesNotExist:
            raise self.model.DoesNotExist

    def get(self, request, slug=None):
        if slug is not None:
            try:
                context = {
                    'form': self.form_class(),
                    f'{self.model_name}': self.get_model_object(slug)
                }
                return render(request, self.template_name, context)
            except self.model.DoesNotExist:
                raise Http404(f'Object for slug "{slug}" does not exist!')
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

    def post_update(self, request, slug):
        form = self.form_class(request.POST)
        if form.is_valid():
            updated_object = form.save()
            return redirect(updated_object)
        else:
            try:
                context = {
                    'form': form,
                    'self.model_name': self.get_model_object(slug),
                }
                return render(request, self.template_name, context)
            except self.model_name.DoesNotExist:
                raise Http404(f'Object for slug "{slug}" does not exist!')

    def post_delete(self, request, slug):
        try:
            self.get_model_object(slug).delete()
            return redirect(f'{self.model_name}_list')
        except self.model_name.DoesNotExist:
            raise Http404(f'Object for slug "{slug}" does not exist!')


class CreateObjectMixin(MethodsForHttpRequestsMixin):

    def post(self, request):
        return self.post_create(request)


class UpdateObjectMixin(MethodsForHttpRequestsMixin):

    def post(self, request, slug):
        return self.post_update(request, slug)


class DeleteObjectMixin(MethodsForHttpRequestsMixin):

    def post(self, request, slug):
        return self.post_delete(request, slug)
