from django.conf.urls import patterns, include, url
from hello import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',('^wwj/$',views.foursuper),
    # Examples:
    # url(r'^$', 'wwj.views.home', name='home'),
    # url(r'^wwj/', include('wwj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
