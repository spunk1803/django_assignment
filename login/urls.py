from django.conf.urls import include, url
from . import views

urlpatterns=[
	url(r'^home/$', views.home,name='home'),
	url(r'^login/$',views.login,name='login'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^profile/$',views.profile, name='profile'),
#	url(r'^profile/(?P<pk>\w+)/$', 'login.views.profile', name='profile'),
#	url(r'^home/$', 'login.views.home', name='home'),
	url(r'^change/', 'login.views.changepass', name='changepass'),
	url(r'^signout/$','login.views.signout',name='signout'),
]
