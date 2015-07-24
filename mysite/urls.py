from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^login/', include('login.urls')),
    url(r'^polls/', include('polls.urls')),	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/',include('contacts.urls')),
#    url(r'^login_new/', include('login_new.urls'))
]
