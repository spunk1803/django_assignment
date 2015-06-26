from django.shortcuts import render
from contacts.models import Contact
from django.views.generic import ListView, CreateView, UpdateView

class ListContactView(ListView):
	model=Contact
	template_name='contact_list.html'

class CreateContactView(CreateView):
	model=Contact
	template_name='edit_contact.html'

	def get_success_url(self):
		return reverse('contacts-list')

class EditContactView(UpdateView):
	model=Contact
	template_name='edit_contact'

	def get_success_url(self):
		return reverse('contacts-list')

