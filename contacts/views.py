from django.shortcuts import render, redirect
from contacts.models import Contact
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
class ListContactView(ListView):
	model=Contact
	template_name='contact_list.html'

class CreateContactView(CreateView):

    model = Contact
    template_name = 'new_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class ContactView(DetailView):

    model = Contact
    template_name = 'contact.html'

