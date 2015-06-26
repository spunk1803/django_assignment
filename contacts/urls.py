from django.conf.urls import patterns,include,url
import views

urlpatterns = [
	url(r'', views.ListContactView.as_view(), name='contacts-list'),
	url(r'^new/$', views.CreateContactView.as_view(), name='contacts-new'),	
	url(r'^edit/$', views.EditContactView.as_view(), name='contacts-edit'),
]
