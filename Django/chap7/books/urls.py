from django.conf.urls import patterns, include, url
from views import hello
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^hello$',hello),
    # Examples:
    # url(r'^$', 'chap7.views.home', name='home'),
    # url(r'^chap7/', include('chap7.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
