from django.conf.urls import patterns, include, url
from views import contact,thank


urlpatterns = patterns('',
    ('',contact),
    ('^thank/',thank),
    #(r'^search-form/$',search_form),
    # Examples:
    # url(r'^$', 'threesuper.views.home', name='home'),
    # url(r'^threesuper/', include('threesuper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
)

