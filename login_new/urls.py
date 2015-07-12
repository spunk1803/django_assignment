from django.conf.urls import include,url,patterns
import views

urlpatterns=[
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^logout/(?P<pk>\d+)/$', views.LogoutView.as_view(), name='logout'),
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^profile/(?P<pk>\d+)/$',views.ProfileView.as_view(), name='profile'),
	url(r'^update/(?P<pk>\d+)/$', views.UpdateView.as_view(), name='update' ),
	url(r'^signup/$', views.CreateProfileView.as_view(), name='signup')
]
