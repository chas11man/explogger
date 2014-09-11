from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'log.views.home', name='home'),
    url(r'^register/', 'log.views.register', name='register'),
    url(r'^logout/', 'log.views.user_logout', name='logout'),
    url(r'^login/', 'log.views.user_login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
)
