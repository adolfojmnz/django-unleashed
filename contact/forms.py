from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import BadHeaderError, mail_managers


class ContactForm(forms.Form):
	CORRECTION = 'C'
	FEEDBACK = 'F'
	SUPPORT = 'S'
	REASON_CHOICES = (
		(CORRECTION, 'Correction'),
		(FEEDBACK, 'Feedback'),
		(SUPPORT, 'Support'),
	)
	reason = forms.ChoiceField(choices=REASON_CHOICES, initial=FEEDBACK)
	email = forms.EmailField(initial='email-address@domain.com')
	text = forms.CharField(widget=forms.Textarea)

	def send_email(self):
		reason = self.cleaned_data['reason']
		reason_dict = dict(self.REASON_CHOICES)
		full_reason = reason_dict.get('reason')
		email = self.cleaned_data['email']
		text = self.cleaned_data['text']
		body = f'Message from {email}: \n\n{text}'
		try:
			mail_managers(full_reason, body)
		except BadHeaderError:
			self.add_error(
				None,
				ValidationError(
					'Could Not Sent Email\n'
					'Extra Header not allowed in email body',
					code='badheader'
				)
			)
			return False
		return True
