from django.conf.urls import patterns, include, url
# sample for testing git poller
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fk.views.home', name='home'),
    # url(r'^fk/', include('fk.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
