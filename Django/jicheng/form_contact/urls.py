from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    ('^thank$',thank),
    ('',form_contact),
    #('^four/',foursuper),
    #('^info/$',display_meta),
    #('^info2/$',display_meta2),
    #('^view',view),
    #('^agent/$',agent),
    #(r'^search-form/$',search_form),
    #(r'^search/$',search),
    # Examples:
    # url(r'^$', 'threesuper.views.home', name='home'),
    # url(r'^threesuper/', include('threesuper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    #(r'^contact/',include('contact.urls')),
    #(r'^form_contact/',include('form_contact.urls))
)


