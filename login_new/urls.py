from django.conf.urls import include,url,patterns
import views

urlpatterns=[
	url(r'^$', views.HomeView, name='home'),
	url(r'^logout/$', views.LogoutView, name='logout'),
	url(r'^login/$', views.LoginView, name='login'),
	url(r'^profile/(?P<pk>\d+)/$',views.ProfileView.as_view(), name='profile'),
	url(r'^update/(?P<pk>\d+)/$', views.UpdateView.as_view(), name='update' ),
	url(r'^signup/$', views.CreateProfileView.as_view(), name='signup')
]
