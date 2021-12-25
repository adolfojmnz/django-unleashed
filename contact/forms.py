from django import forms


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
		body = f'Message from {email}: \n\nSubject: {full_reason}\n{text}'
