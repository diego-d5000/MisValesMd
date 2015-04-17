from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

	def save(self, user, *args, **kwargs):
		self.instance.user = user
		super(PersonForm, self).save(*args, **kwargs)

	class Meta:
		model = Person
		exclude = ('user', )
		# fields