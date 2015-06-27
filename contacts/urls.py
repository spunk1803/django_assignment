from django.conf.urls import patterns,include,url
import views

urlpatterns = [
	url(r'', views.ListContactView.as_view(), name='contacts-list'),
	url(r'^new/$', views.CreateContactView.as_view(), name='contacts-new'),	
	url(r'^edit/$', views.EditContactView.as_view(), name='contacts-edit'),
	url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(), name='contacts-view',),
	url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(), name='contacts-delete',),
	url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(), name='contacts-edit',),


]
