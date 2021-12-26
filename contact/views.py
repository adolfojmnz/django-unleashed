from django.shortcuts import render, redirect
from django.contrib.messages import success
from django.views.generic import View

from .forms import ContactForm


class ContactView(View):
	form_class = ContactForm
	template_name = 'contact/contact.html'

	def get(self, request):
		context = {'form': self.form_class()}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			email = form.send_email()
			if email:
				print('Email sent!')
				success(request, 'Email Successfully Sent!')
				return redirect('post_list')
		else:
			context = {'form': form}
			return render(request, self.template_name, context)
